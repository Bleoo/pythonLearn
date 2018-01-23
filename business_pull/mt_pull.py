# -*- coding: utf-8 -*-

import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from business_pull.area import Area
from business_pull.city import City

url_prefix = 'http://'
url_suffix = '.meituan.com/meishi/'


def get_pop_content(page_source, area):
    result_soup = BeautifulSoup(page_source, 'html.parser')  # 然后将其解析
    business_soup = result_soup.find('div', class_='popover')
    business_soup = business_soup.find('div', class_='p-content')
    business_soup = business_soup.find_all('a')
    sub_area = []
    for a in business_soup:
        # print(a.string)
        sub_area.append(a.string)
    area.set_sub_area(','.join(sub_area))


def find_business_list(url):
    try:
        driver.get(url)
        left = driver.find_element_by_class_name('left')
        condition = left.find_element_by_class_name('condition')
        business_list = condition.find_elements_by_class_name('cont')
        business_list = business_list[1].find_element_by_class_name('more')
        # print(business_list.text)
        return business_list
    except:
        return None


def perform_element(business_list):
    try:
        list_area = []
        list_b = business_list.find_elements_by_tag_name('b')
        for ele in list_b:
            # print(ele.text)
            area = Area(ele.text)
            ActionChains(driver).move_to_element(ele).perform()
            time.sleep(0.3)
            get_pop_content(driver.page_source, area)  # 这是原网页 HTML 信息
            list_area.append(area)
            # print(area)
        return list_area
    except:
        return None


def get_all_city():
    driver.get("http://www.meituan.com/changecity/")
    result_soup = BeautifulSoup(driver.page_source, 'html.parser')  # 然后将其解析
    result_soup = result_soup.find('div', class_='alphabet-city-area')
    result_soup = result_soup.find_all('a')
    list_city = []
    for a_link in result_soup:
        print(a_link.string)
        city = City(a_link.string)
        business_list = find_business_list("http:" + a_link.get('href') + "/meishi/")
        if business_list is None:
            continue
        area = perform_element(business_list)
        if area is None:
            continue
        city.set_area(area)
        list_city.append(city)
        time.sleep(1.5)
    print(list_city)


def main():
    global driver
    driver = webdriver.Chrome('/Users/bleoo/Downloads/chromedriver')  # 打开浏览器
    driver.get("https://www.meituan.com")
    get_all_city()
    # driver.get("http:" + "//arongqi.meituan.com" + "/meishi/")
    # business_list = find_business_list()
    # area = perform_element(business_list)


if __name__ == '__main__':
    main()
