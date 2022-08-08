# -*- coding:utf-8 -*-
# @Project: cema
# @Time : 2022/8/2 下午12:38
# @Author : yxl
# @File : music.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
# option = webdriver.ChromeOptions()
# option.page_load_strategy = 'none'
driver.implicitly_wait(5)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false
    })
    """
})
driver.get("http://music.163.com/")
# driver.find_element('link text', '登陆').click()

# driver.implicitly_wait(5)
# driver.get('http://y.qq.com/')
# driver.get("http://1.12.218.8/fsmarket/")
# sleep(3)
# driver.find_element('id', 'recommend_title').click()
# js = "arguments[0].scrollerToView()"
# driver.execute_script(js, el)
# sleep(3)
# driver.quit()
# driver.maximize_window()
# sleep(3)
# driver.find_element('link text', '我的音乐').click()
driver.find_element('link text', '创作者中心').click()

print('执行结束')

sleep(7)

driver.quit()

# e = WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element('link text', '登陆'), message='显示等等失败')
# e.click()
# driver.find_element('link text', 'MV').click()
# driver.find_element('class name', 'link s-fc3').click()
# sleep(2)

# driver.quit()

# driver.find_element("xpath", '//*[@id="auto-id-0oc1ytbd7uU9X4gT"]/a').click()
# handles = driver.window_handles
# driver.close()
# driver.switch_to.window(handles[1])
# driver.find_element("link text", "选择其他登录模式").click()
# driver.find_element("id", "j-official-terms").click()
# driver.find_element("link text", "网易邮箱帐号登录").click()


# alert = driver.switch_to.alert
# alert.accept()
# alert.dismiss()
# alert.send_keys()
# alert.text

# key = Keys('Chrome')

