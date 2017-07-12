__author__ = 'Woody'
import redis


class Redis(object):

    def __init__(self):
        self.redisManager = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get(self, name):
        return self.redisManager.get(name).decode("utf-8")

    def setAppLaunch(self, value):
        return self.redisManager.set("Android", value)

    def getAppLauch(self):
        return self.redisManager.get("Andorid").decode("utf-8")

    def set(self, name, value):
        return self.redisManager.set(name, value)