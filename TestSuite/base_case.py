__author__ = 'Woody'
'''测试用例基类,其他新写的用例从此处继承

'''

import unittest
from Common.WebMethod import AppDriver
from setting import *
from Common.mongo_operator import MongoClient
from Common.RedisModule import Redis
from appium import webdriver


class BaseNeedLogin(unittest.TestCase):
    case_num = 1
    case_id = None
    # 获取driver
    driver = webdriver.Remote(local_appium, desired_caps_real)
    # 创建mongo客户端连接
    db = MongoClient()
    login_case = "Case000"
    driver = AppDriver(driver, location=db.get_case_location(login_case))

    @classmethod
    def setUpClass(cls):
        cls.case_id = cls.__name__
        # 获取case元素定位信息
        # 模拟登陆
        cls.driver.click_text("系统权限允许按钮")
        cls.driver.click_text("系统权限允许按钮")
        cls.driver.click("欢迎页-跳过按钮")
        cls.driver.send("首页-用户名输入框")
        cls.driver.send("首页-密码输入框")
        cls.driver.click("首页-登录按钮")
        cls.location = cls.db.get_case_location(cls.case_id)

    @classmethod
    def tearDownClass(cls):
        case_num = int(Redis().get("case_num"))
        case_num -= cls.case_num
        Redis().set("case_num", case_num)
        if not case_num:
            if cls.driver:
                cls.driver.quit()
            if cls.db:
                cls.db.Client.close()


class Base(BaseNeedLogin):

    @classmethod
    def setUpClass(cls):
        cls.case_id = cls.__name__
        cls.location = cls.db.get_case_location(cls.case_id)







