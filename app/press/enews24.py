import time

from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import itertools
from app import db, text_cleaner, keywords
from app.models import Article


# print(driver.current_url)


def get_link_from_news_title(keyword, type, press):

    downloadDestination = 'http://enews24.tving.com/search?bCode=13&searchTerm='

    # dir = r'/etc/apt/sources.list.d/google.list'
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(downloadDestination)

    # driver.find_element_by_xpath('//*[@id="header_tving"]/div[1]/div/div[4]/button').click()
    driver.find_element_by_xpath('//*[@id="search"]').send_keys(keyword)
    # driver.find_element_by_name('kw').send_keys(keyword)
    driver.find_element_by_xpath('//*[@id="sendSearch"]').click()
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/button').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/button').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for a in driver.find_elements_by_xpath('//*[@id="container"]/div/div/div/div/ul/li/div/a'):
        # print(a.get_attribute('href'))
        url = a.get_attribute('href')
        str_url = str(url)
        print(str_url)

        # if len(str_url) < 44:
        source_code_from_url = urllib.request.urlopen(str_url)
        soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
        content_of_article = soup.select('div.articleContents')
        print(content_of_article)
        # for item in content_of_article_title + content_of_article:
        for item in content_of_article:
            # print(item)
            string = str(item.find_all(text=True))
            string_item = text_cleaner.clean_text(string)
            a = Article(title_name=str_url, body=string_item, type=type, press=press)
            db.session.add(a)
            db.session.commit()
            print('#####################Success######################')


def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '엑소'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '비투비'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '세븐틴'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '뉴이스트'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '트와이스'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '레드벨벳'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')