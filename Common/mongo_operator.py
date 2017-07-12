__author__ = 'Woody'
import pymongo
import logging
from bson import ObjectId
from setting import *


class MongoClient(object):

    def __init__(self):
        try:
            self.Client = pymongo.MongoClient(host=HOST, port=PORT)
            self.db = self.Client.yitu8
            assert self.db.authenticate(user, pwd), "mongo服务器连接失败!"
        except Exception as err:
            logging.error("mongo connect error: {}".format(str(err)))

    def __del__(self):
        self.Client.close()

    def get_db(self):
        return self.db

    def get_case_location(self, case_id):
        return self.db.ui_case.find_one({"case_id": case_id})

