__author__ = 'Woody'

from TestSuite.base_case import Base
from Common.WebMethod import auto_pic



class Case002(Base):
    test_des = "司导端进入聊天页面"

    @auto_pic
    def test(self):
        self.case_id = self.__class__.__name__
        location = self.db.get_case_location(self.case_id)
        self.driver.click(**location.get('聊天按钮'))
        # self.driver.click_text(**location.get('我的车辆按钮'))
        # pass

