# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import os
import time
import datetime

from aion.microservice import main_decorator, Options
from aion.kanban import Kanban
from aion.logger import lprint, initialize_logger

from .yaskawa_maintenace_mysql_model import YaskawaMaintenaceMysqlModel
from .yaskawa_robot_mongo_model import YaskawaMaintenaceMongodbModel

SERVICE_NAME = "set-alarm-history-to-sql-yaskawa"
# DEVICE_NAME = os.environ.get("DEVICE_NAME")
initialize_logger(SERVICE_NAME)

YASKAWA_ALARM_CATEGORY_SIZE = 5
INTERVAL = 1.0


def make_alarm(alarm, category):
    return {
        'code': alarm['AlarmCode'],
        'data': alarm['AlarmData'],
        'name': alarm['AlarmName'],
        'created': alarm['AlarmTime'],
        'type': alarm['AlarmType'],
        'category': category
    }

def get_new_alarm(db_alarms, latest_alarms, category):
    new_alarm = []
    for alarm in latest_alarms:
        if not (alarm['AlarmTime'] and alarm['AlarmCode']):
            continue
        is_same_alarm = any(list(map(lambda db_alarm: alarm['AlarmCode'] == db_alarm['AlarmCode']
                                        and datetime.datetime.strptime(alarm['AlarmTime'], '%Y/%m/%d %H:%M') == db_alarm['AlarmTime']
                                    , db_alarms)))
        if not is_same_alarm:
            new_alarm.append(make_alarm(alarm, category))

    return new_alarm

def arrangeAlarmByCategory(alarms):
    """
    故障履歴をカテゴリ毎に分ける
    ArrayNo     :   カテゴリー              : カテゴリーNo
    ----------------------------------------------
    1~100       :   重故障                 ：   1
    1001~1100   :   軽故障                 ：   2
    2001~2100   :   ユーザアラーム(システム） ：   3
    3001~3100   :   ユーザアラーム(ユーザ)   ：   4
    4001~4100   :   オフラインアラーム       ：   5
    """
    category1 = list(filter(lambda alarm: alarm.get('ArrayNo') > 0    and  alarm.get('ArrayNo') <= 100, alarms))
    category2 = list(filter(lambda alarm: alarm.get('ArrayNo') > 1000 and  alarm.get('ArrayNo') <= 1100, alarms))
    category3 = list(filter(lambda alarm: alarm.get('ArrayNo') > 2000 and  alarm.get('ArrayNo') <= 2100, alarms))
    category4 = list(filter(lambda alarm: alarm.get('ArrayNo') > 3000 and  alarm.get('ArrayNo') <= 3100, alarms))
    category5 = list(filter(lambda alarm: alarm.get('ArrayNo') > 4000 and  alarm.get('ArrayNo') <= 4100, alarms))

    return category1, category2, category3, category4, category5

def extractAlarm(alarm_cur):
    try:
        alarm_data = alarm_cur.next()
        data = alarm_data['metadata']['RobotData']['RobotData']
    except:
        return None
    return data


@main_decorator(SERVICE_NAME)
def main_without_kanban(opt: Options):
    lprint("start main_without_kanban()")
    # get cache kanban
    conn = opt.get_conn()
    num = opt.get_number()
    kanban: Kanban = conn.set_kanban(SERVICE_NAME, num)

    ######### main function #############
    while True:
        # mongodbから最新の異常履歴を取得
        with YaskawaMaintenaceMongodbModel() as mongodb:
            alarm_cur = mongodb.get_latest_alarm()
            latest_alarm_data = extractAlarm(alarm_cur)
            # 故障カテゴリ毎にまとめる
            latest_alarm_data = arrangeAlarmByCategory(latest_alarm_data)
            if not latest_alarm_data:
                lprint("Not found alarm data")
                time.sleep(INTERVAL)
                continue

        with YaskawaMaintenaceMysqlModel() as db:
            # mysqlから保持している最新の異常履歴を取得
            for i in range(YASKAWA_ALARM_CATEGORY_SIZE):
                category_no = i + 1
                db_alarm_data = db.getLatest_N(category_no, 10)

                # 新しい異常履歴を取得
                new_alarms = get_new_alarm(db_alarm_data, latest_alarm_data[i], category_no)
                for new_alarm in new_alarms:
                    db.append(new_alarm)

                if new_alarms:
                    db.commit_query()
                    lprint(f"new alarm history has been saved: {str(new_alarms)}")

        time.sleep(INTERVAL)