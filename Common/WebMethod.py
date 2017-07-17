__author__ = 'Woody'

import logging
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Common.AppiumTools import Tools
from exceptions.ElementException import eleException

TIMEOUT = 20


def wait(func):
    def wrapper(*args, **kwargs):
        driver = args[0].driver
        location = args[0].location
        key = args[1]
        method = location[key].get('method')
        value = location[key].get('value')
        try:
            WebDriverWait(driver, TIMEOUT).until(
                lambda x: x.find_element(by=getattr(By, method), value=value))
            return func(*args, **kwargs)
        except Exception as err:
            raise eleException("等待元素[{}]出错!请检查! 错误原因: {}".format(key, str(err)))
    return wrapper


def auto_pic(func):
    def wrapper(*args, **kwargs):
        driver = args[0].driver.driver
        # 更新case配置
        args[0].driver.location = args[0].db.get_case_location(args[0].case_id)
        case_id = args[0].case_id
        try:
            return func(*args, **kwargs)
        except eleException as err:
            logging.error("func {} error: {}".format(func.__name__, str(err)))
            raise eleException(err)
        except Exception as err:
            raise Exception("case_id: [{}] 运行出错, 详情: {}".format(case_id, str(err)))
        finally:
            t = Tools(driver)
            t.get_pic(case_id)
    return wrapper


class AppDriver(object):

    def __init__(self, driver, location):
        self.driver = driver
        self.location = location

    def id_find(self, _id):
        return self.driver.find_element_by_id(_id)

    @wait
    def id_finds(self, key):
        method = self.location[key]['method']
        value = self.location[key]['value']
        return self.driver.find_elements(by=getattr(By, method), value=value)


    def xpath_find(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def css_find(self, css):
        return self.driver.find_element_by_css_selector(css)

    def class_find(self, class_):
        return self.driver.find_elements_by_class_name(class_)

    @wait
    def click_text(self, key):
        method = self.location[key]['method']
        value = self.location[key]['value']
        text = self.location[key]['text']
        eles = self.driver.find_elements(by=getattr(By, method), value=value)
        for ele in eles:
            if ele.text == text:
                ele.click()
                break

    @wait
    def click(self, key):
        method = self.location[key]['method']
        value = self.location[key]['value']
        self.driver.find_element(getattr(By, method), value).click()

    @wait
    def send(self, key):
        method = self.location[key]['method']
        value = self.location[key]['value']
        text = self.location[key]['text']
        self.driver.find_element(getattr(By, method), value).send_keys(text)

    @property
    def height(self):
        return self.driver.get_window_size().get('height')

    @property
    def width(self):
        return self.driver.get_window_size().get('width')

    def clear(self, key):
        method = self.location[key]['method']
        value = self.location[key]['value']
        self.driver.find_element(getattr(By, method), value).clear()

    def quit(self):
        self.driver.quit()

    def notification(self):
        self.driver.open_notifications()



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



