__author__ = 'Woody'

import os
from datetime import datetime
from setting import pic_dir


class Tools(object):
    '''
    封装部分appium-driver的办法
    tool = Tools()
    tool.get_pic()  # 截图
    '''

    def __init__(self, driver):
        '''
        传入driver实例, 封装driver的方法
        :param driver:
        '''
        self.driver = driver

    def get_pic(self, case_id=None):
        '''
        截图方法
        :param case_id:
        :return:
        '''
        pic = os.path.join(pic_dir, case_id) if case_id else pic_dir
        if not os.path.exists(pic):
            os.mkdir(pic)
        self.driver.get_screenshot_as_file(
            os.path.join(pic, "{}.png".format(datetime.strftime(datetime.now(), "%Y-%m-%d %H-%M-%S"))))


