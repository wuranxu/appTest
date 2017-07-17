__author__ = 'Woody'

from TestSuite.base_case import BaseNeedLogin
from Common.WebMethod import auto_pic
import unittest

class Case001(BaseNeedLogin):
    test_des = "进入我的管理页面"
    test_notify_des = "异常测试"
    test_2321_des = "跳过测试"
    case_num = 3

    @auto_pic
    def test(self):
        self.driver.click('我的管理按钮')
        self.driver.click_text('我的车辆按钮')
        cars = self.driver.id_finds("我的车辆数量")
        for index, car in enumerate(cars):
            print("我的第{}辆车是: {}".format(index+1, car.text))


    @auto_pic
    def test_notify(self):
        pass

    @unittest.skip("这个Case暂时屏蔽!")
    def test_2321(self):
        pass
