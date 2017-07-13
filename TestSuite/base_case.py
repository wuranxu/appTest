__author__ = 'Woody'
'''测试用例基类,其他新写的用例从此处继承

'''

import unittest
from Common.WebMethod import driver
from setting import *
from Common.LoginModule import Login
from Common.mongo_operator import MongoClient
from Common.RedisModule import Redis


class BaseNeedLogin(unittest.TestCase):

    case_id = None
    # driver = None
    # 获取driver
    dr = driver(local_appium, desired_caps_real)
    driver = Login(dr).driver
    # 创建mongo客户端连接
    db = MongoClient()

    '''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            orig = super(BaseNeedLogin, cls)
            cls.instance = orig.__new__(cls)
        return cls.instance'''

    @classmethod
    def setUpClass(cls):
        login_case = "Case000"
        cls.case_id = cls.__name__
        # 获取case元素定位信息
        location = cls.db.get_case_location(login_case)
        # 模拟登陆
        cls.driver.click_text(**location.get("系统权限允许按钮"))
        cls.driver.click_text(**location.get("系统权限允许按钮"))
        cls.driver.click(**location.get("欢迎页-跳过按钮"))
        cls.driver.send(**location.get("首页-用户名输入框"))
        cls.driver.send(**location.get("首页-密码输入框"))
        cls.driver.click(**location.get("首页-登录按钮"))

    @classmethod
    def tearDownClass(cls):
        case_num = int(Redis().get("case_num"))
        case_num -= 1
        Redis().set("case_num", case_num)
        if not case_num:
            if cls.driver:
                cls.driver.quit()
            if cls.db:
                cls.db.Client.close()


class Base(BaseNeedLogin):

    @classmethod
    def setUpClass(cls):
        pass







