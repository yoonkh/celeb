from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import itertools
from app import db, text_cleaner, keywords
from app.models import Article


# print(driver.current_url)


def get_link_from_news_title(keyword, type, press):

    try:
        downloadDestination = 'http://www.sportsseoul.com'

        # dir = r'/etc/apt/sources.list.d/google.list'
        driver = webdriver.Chrome('/usr/bin/chromedriver')
        driver.get(downloadDestination)

        driver.find_element_by_name("search_txt").send_keys(keyword)
        driver.find_element_by_class_name("btn_search").click()

        for a in driver.find_elements_by_xpath('//*[@id="SearchLists"]/div/div/div/div/dl/dt/a'):
            print(a.get_attribute('href'))
            url = a.get_attribute('href')
            str_url = str(url)

            if len(str_url) < 44:
                source_code_from_url = urllib.request.urlopen(str_url)
                soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
                content_of_article = soup.select('span.bk_article_view')
                # print(content_of_article)
                # for item in content_of_article_title + content_of_article:

                title = soup.select('div.viewtitle')

                title_item = ""

                for t in title:
                    string = str(t.find_all(text=True))
                    title_item = text_cleaner.clean_text(string)


                for item in content_of_article:
                    # print(item)
                    string = str(item.find_all(text=True))
                    string_item = text_cleaner.clean_text(string)
                    a = Article(title_name=title_item, title_link=str_url, body=string_item, type=type, press=press)
                    db.session.add(a)
                    db.session.commit()
    except Exception:
        pass


def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords3:
        print(keyword)
        type = '엑소'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords4:
        print(keyword)
        type = '비투비'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords5:
        print(keyword)
        type = '세븐틴'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords6:
        print(keyword)
        type = '뉴이스트'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords7:
        print(keyword)
        type = '트와이스'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)

    for keyword in keywords.keywords8:
        print(keyword)
        type = '레드벨벳'
        press = '스포츠서울'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press)