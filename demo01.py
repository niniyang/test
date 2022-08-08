# -*- coding:utf-8 -*-
# @Project: cema
# @Time : 2021/10/28 下午2:35
# @Author : yxl
# @File : demo01.py
from time import sleep

from selenium import webdriver

# def test01():
#     print("test01")
#
# def test02():
#     print("test02")

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
el = driver.find_element('id', 'kw')
el.send_keys('test')

driver.find_element('id', 'su').click()

sleep(3)

driver.quit()

# //*[@id="su"]
# //*[@id="mCon"]/span