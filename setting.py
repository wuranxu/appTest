__author__ = 'Woody'

local_appium = 'http://localhost:4723/wd/hub'

desired_caps_real = {
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "HEE6R15C17002984",
    "appPackage": "net.yitu8.drivier",
    "appActivity": ".modles.WelcomeActivity",
    "newCommandTimeout": 200
}

desired_caps_vir = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "net.yitu8.drivier",
    "appActivity": ".modles.WelcomeActivity",
    "newCommandTimeout": 200

}

HOST = 'localhost'
PORT = 27017
user = 'yitu8'
pwd = 'yitu8'

pic_dir = r"E:\AppTest\ErrorPic"


