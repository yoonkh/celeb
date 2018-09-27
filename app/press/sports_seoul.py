from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time
import urllib.request

# downloadDestination = 'https://www.instagram.com/fitness/'  # 다운받을 주소

downloadDestination = 'http://www.sportsseoul.com'
coreCount = 8  # 스크롤할 양

# dir = r'/etc/apt/sources.list.d/google.list'
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get(downloadDestination)
driver.find_element_by_name("search_txt").send_keys('워너원')
driver.find_element_by_class_name("btn_search").click()
# print(driver.current_url)
for a in driver.find_elements_by_xpath('.//*[@id="SearchLists"]//a'):
    print(a.get_attribute('href'))
    url = a.get_attribute('href')

    if len(url) < 44:
        source_code_from_url = urllib.request.urlopen(url)
        soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
        content_of_article = soup.select('span.bk_article_view')
        print(content_of_article)
        # for item in content_of_article_title + content_of_article:
        for item in content_of_article:
            print(item)
            string_item = str(item.find_all(text=True))

            print(string_item)