# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import re
import aion.mongo as mongo

MONGO_DB_NAME = "AionCore"
COLLECTION_NAME = "kanban"
STREAM_KEY = "kanban:after:control-yaskawa-robot-r"

class YaskawaMaintenaceMongodbModel(mongo.BaseMongoAccess):
    def __init__(self):
        super().__init__(MONGO_DB_NAME)
        self._collection_name = COLLECTION_NAME

    def get_latest_alarm(self, timestamp=None):
        key_regex = re.compile(
            "^%s" % STREAM_KEY , re.IGNORECASE)
        
        fi = {'metadata.RobotData.Command' : '71'}
       
        if timestamp is not None:
            fi['finishAt'] = {'$gt': timestamp}

        # return type is cursor
        return self.find(
            self._collection_name,
            filter=fi,
            sort=[('finishAt', -1)] # desc
        ).limit(1)


if __name__ == '__main__':

    class Mongo(mongo.BaseMongoAccess):
        def get_one(self):
            fi = {}
            return self.find('startup_log', filter=fi).limit(1)

        def get_alarm(self):
            fi = {'metadata.RobotData.Command' : '71'}
            return self.find('kanban', filter=fi).limit(4)
            
        with YaskawaMaintenaceMongodbModel() as db:
            ret = db.get_latest_alarm()
            print(ret)

    print("access mongo")
    with Mongo(MONGO_DB_NAME) as db:
        find = db.get_alarm()
        for doc in find:
            print(doc['metadata']['RobotData']['RobotData'])

    print("finish mongo")
    
