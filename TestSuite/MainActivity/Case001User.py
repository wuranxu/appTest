__author__ = 'Woody'
from TestSuite.base_case import BaseNeedLogin
from Common.WebMethod import auto_pic
import unittest

class Case001(BaseNeedLogin):
    test_des = "进入我的管理页面"
    test_222_des = "异常测试"
    test_2321_des = "跳过测试"
    case_num = 3

    @auto_pic
    def test(self):
        location = self.db.get_case_location(self.case_id)
        self.driver.click(**location.get('我的管理按钮'))
        self.driver.click_text(**location.get('我的车辆按钮'))

    def test_222(self):
        return 2 / 0

    @unittest.skip("This is a skipped test.")
    def test_2321(self):
        pass
