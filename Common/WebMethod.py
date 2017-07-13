__author__ = 'Woody'

import logging
from appium import webdriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Common.AppiumTools import Tools

TIMEOUT = 10


def wait(func):
    def wrapper(*args, **kwargs):
        driver = args[0]
        method = kwargs.get('method')
        value = kwargs.get('value')
        try:
            WebDriverWait(driver, TIMEOUT).until(
                lambda x: x.find_element(by=getattr(By, method), value=value))
            func(*args, **kwargs)
        except Exception as err:
            raise Exception("等待元素{}出错!请检查! 错误原因: {}".format(value, str(err)))
    return wrapper


def auto_pic(func):
    def wrapper(*args, **kwargs):
        driver = args[0].driver
        case_id = args[0].case_id
        try:
            func(*args, **kwargs)
        except Exception as err:
            logging.error("func {} error: {}".format(func.__name__, str(err)))
            # raise Exception("case_id: {} 运行出错, 详情: {}".format(case_id, str(err)))
            assert 0, "出错啦啊啊啊啊啊"
        finally:
            t = Tools(driver)
            t.get_pic(case_id)
    return wrapper


class driver(webdriver.Remote):

    def id_find(self, _id):
        return self.find_element_by_id(_id)

    def xpath_find(self, xpath):
        return self.find_element_by_xpath(xpath)

    def css_find(self, css):
        return self.find_element_by_css_selector(css)

    @wait
    def click_text(self, method, value, text):
        eles = self.find_elements(by=getattr(By, method), value=value)
        for ele in eles:
            if ele.text == text:
                ele.click()
                break

    @wait
    def click(self, method, value):
        self.find_element(getattr(By, method), value).click()

    @wait
    def send(self, method, value, text):
        self.find_element(getattr(By, method), value).send_keys(text)


class element(object):

    def __init__(self, WebElementObj):
        if isinstance(WebElementObj, WebElement):
            self.ele = WebElementObj
        else:
            raise Exception("请传入WebElement对象!")

    def send(self, value):
        self.ele.send_keys(value)

    def clear(self):
        self.ele.clear()

    def attr(self, attribute):
        return self.ele.get_attribute(attribute)



