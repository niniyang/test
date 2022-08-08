# -*- coding:utf-8 -*-
# @Project: cema
# @Time : 2022/8/3 下午2:51
# @Author : yxl
# @File : keys.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Keys:
    # driver = webdriver.Chrome();

    def __init__(self, browser_type):
        self.open_browser(browser_type)
        self.driver.implicitly_wait(5)

    def open_browser(browser_type):
        try:
            if browser_type == 'Chrome':
                driver = webdriver.Chrome(options=None)
            else:
                driver = getattr(webdriver, browser_type)()
        except:
            driver = webdriver.Chrome()
        return driver

    def open(self, url):
        self.driver.get(url)

    def locate(self, by, value):
        return self.driver.find_element(by, value)

    def input(self, by, value, txt):
        self.locate(by, value).send_keys(txt)

    def click(self, by, value):
        self.locate(by, value).click()

    def quit(self):
        self.driver.quit()

    # 文本断言
    def assert_text(self, by, value, expected):
        try:
            real = self.locate(by, value).text
            assert expected == real, '{0}与{1}不相等'.format(real, expected)
        except Exception as e:
            print('断言失败：{}'.format(e))

    # 预期结果是否包含在实际结果内
    def assert_almost_equal(self, by, value, expected):
        try:
            real = self.locate(by, value).text
            assert expected in real, '{0}不在{1}范围内'.format(expected, real)
            return True
        except:
            return False

    def driver_wait(self, by, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locate(by, value), message='元素获取失败')

    def sleep(self, time):
        sleep(time)

    # 句柄切换，为了满足y有些场景下不需要close，需要考虑逻辑的处理
    def switch_handle(self, status=1):
        handles = self.driver.window_handles
        if status == 1:
            self.driver.close()
        self.driver.switch_to.window(handles[1])
