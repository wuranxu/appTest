__author__ = 'Woody'
from TestSuite.base_case import BaseNeedLogin


class Case001(BaseNeedLogin):

    def test(self):
        # self.case_id = self.__class__.__name__
        location = self.db.get_case_location(self.case_id)
        self.driver.click(**location.get('我的管理按钮'))
        # self.driver.click_text(**location.get('我的车辆按钮'))
        # pass

