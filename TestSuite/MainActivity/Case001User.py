__author__ = 'Woody'
from TestSuite.base_case import BaseNeedLogin
from Common.WebMethod import auto_pic

class Case001(BaseNeedLogin):

    @auto_pic
    def test(self):
        # self.case_id = self.__class__.__name__
        location = self.db.get_case_location(self.case_id)
        # location.update({"我的管理按钮": None})
        self.driver.click(**location.get('我的管理按钮'))
        # self.driver.click_text(**location.get('我的车辆按钮'))
        # pass

