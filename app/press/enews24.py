import time
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
from app import db, text_cleaner, keywords
from app.models import Article


def get_link_from_news_title(keyword, type, press):

    downloadDestination = 'http://enews24.tving.com/search?bCode=13&searchTerm='
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(downloadDestination)

    try:

        driver.find_element_by_xpath('//*[@id="search"]').send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="sendSearch"]').click()
        driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/a').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/button').click()
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[3]/div[2]/button').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        for a in driver.find_elements_by_xpath('//*[@id="container"]/div/div/div/div/ul/li/div/a'):
            url = a.get_attribute('href')
            str_url = str(url)
            source_code_from_url = urllib.request.urlopen(str_url)
            soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
            content_of_article = soup.select('div.articleContents')
            title = soup.select('h2.title')

            title_item = ""

            for t in title:
                string = str(t.find_all(text=True))
                title_item = text_cleaner.clean_text(string)

            for item in content_of_article:
                string = str(item.find_all(text=True))
                string_item = text_cleaner.clean_text(string)

                article_group = Article(title_name=title_item, title_link=str_url, type=type, press=press, body=string_item)

                db.session.add(article_group)
                db.session.commit()
                print('########################################## 완료 !!! ############################################')

    except Exception:
        pass


def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords3:
        print(keyword)
        type = '엑소'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords4:
        print(keyword)
        type = '비투비'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords5:
        print(keyword)
        type = '세븐틴'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords6:
        print(keyword)
        type = '뉴이스트'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords7:
        print(keyword)
        type = '트와이스'
        k = keyword
        # url = downloadDestination + quote(k)
        get_link_from_news_title(k, type, press='enews24')

    for keyword in keywords.keywords8:
        print(keyword)
        type = '레드벨벳'
        k = keyword
        get_link_from_news_title(k, type, press='enews24')