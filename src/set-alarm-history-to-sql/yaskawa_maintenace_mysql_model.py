import aion.mysql as mysql

ROBOT_ID = 1

class YaskawaMaintenaceMysqlModel(mysql.BaseMysqlAccess):
    def __init__(self):
        super().__init__("Maintenance")

    def append(self, alarm):
        query = f"""
            INSERT INTO alarms_yaskawa (
                robot_id, AlarmCode, AlarmType, AlarmData,
                AlarmTime, AlarmName, AlarmCategory
            ) VALUES (
                {ROBOT_ID}, {int(alarm['code'])}, {int(alarm['type'])}, {int(alarm['data'])},
                '{alarm['created']}', '{alarm['name']}', {int(alarm['category'])}
            );
        """
        self.set_query(query)

    def getLatest_N(self, alarm_category, size):
        query = f"""
            SELECT  * FROM alarms_yaskawa
            WHERE robot_id = {ROBOT_ID} AND AlarmCategory = {alarm_category}
            ORDER BY AlarmTime DESC;
            """

        rs = self.get_query_list(size, query)
        return rs

if __name__ == '__main__':

    alarm = {'code': 4009, 'type': 1, 'data': 99, 
            'created': '2020/07/29 19:10', 'name': '故障名', 'category': 4 }

    with YaskawaMaintenaceMysqlModel() as db:
        ret = db.append(alarm)
        db.commit_query()
        print(f'append alarm to sql')    
