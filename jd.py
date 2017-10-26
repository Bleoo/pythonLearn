# -*- coding: utf-8 -*-

import datetime
import time

from selenium import webdriver

driver = webdriver.Chrome('/Users/bleoo/Downloads/chromedriver')  # 打开浏览器


def readUser():
    with open('/Users/bleoo/Desktop/test.txt', 'r') as f:
        return f.readlines()


def login(uname, pwd):
    driver.get("https://www.jd.com/")
    if driver.find_element_by_class_name("link-login"):
        driver.find_element_by_class_name("link-login").click()
    if driver.find_element_by_link_text("账户登录"):
        driver.find_element_by_link_text("账户登录").click()
    if driver.find_element_by_id("loginname"):
        driver.find_element_by_id("loginname").send_keys(uname)
    if driver.find_element_by_id("nloginpwd"):
        driver.find_element_by_id("nloginpwd").send_keys(pwd)
    if driver.find_element_by_class_name("login-btn"):
        driver.find_element_by_class_name("login-btn").click()
    time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('登录成功！')


def buy_on_time(buyTime):
    print('等待开场...')
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buyTime:
            time.sleep(0.4)
            while True:
                driver.find_element_by_id('order-submit').click()
                time.sleep(0.15)
        time.sleep(0.1)


print('等待登录...')

# while True:
# now = datetime.datetime.now()
# if now.strftime('%Y-%m-%d %H:%M:%S') == '2017-10-25 19:58:00':
list = readUser()
login(list[0], list[1])
buy_on_time('2017-10-25 20:00:00')
# time.sleep(0.3)
