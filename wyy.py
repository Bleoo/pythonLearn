import datetime
import time

from selenium import webdriver

driver = webdriver.Chrome('/Users/bleoo/Downloads/chromedriver')  # 打开浏览器


def login(uname, pwd):
    driver.get("http://music.163.com/store/product")
    if driver.find_element_by_link_text("网易邮箱账号登录"):
        driver.find_element_by_link_text("网易邮箱账号登录").click()
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
            while True:
                driver.find_element_by_class_name('s-fcLink f-hand').click()
                time.sleep(0.5)
        time.sleep(0.5)


print('等待登录...')
login("lyhy22@163.com", "woaini1314")
buy_on_time('2017-10-23 10:00:01')
