import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

from app import text_cleaner, db, keywords
from app.models import Article


TARGET_URL_BEFORE_PAGE_NUM = 'http://www.spotvnews.co.kr/?page='
TARGET_URL_BEFORE_MIDDLE = '&mod=news&act=articleList&sc_area=A'
TARGET_URL_BEFORE_KEYWORD = '&sc_word='


# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, type, press):

    for i in range(page_num):
        current_page_num = i + 1
        position = URL.index('&sc_word=')

        URL_with_page_num = TARGET_URL_BEFORE_PAGE_NUM + str(current_page_num) + TARGET_URL_BEFORE_MIDDLE + URL[position:]
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for title in soup.select('a.list_title_a'):

            title_link = TARGET_URL_BEFORE_PAGE_NUM[:-7] + title['href']
            print(title_link)
            source_code_from_url = urllib.request.urlopen(title_link)
            soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
            print(soup)
            content_of_article = soup.find_all(itemprop="articleBody")

            tit = soup.select('h1.arl_view_title')

            title_item = ""

            for t in tit:
                string = str(t.find_all(text=True))
                title_item = text_cleaner.clean_text(string)

            for item in content_of_article:
                string = str(item.find_all(text=True))
                print(string)
                string_item = text_cleaner.clean_text(string)
                a = Article(title_name=title_item, title_link=title_link, body=string_item, type=type, press=press)
                db.session.add(a)
                db.session.commit()



def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)
    for keyword in keywords.keywords3:
        print(keyword)
        type = '엑소'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)
    for keyword in keywords.keywords4:
        print(keyword)
        type = '비투비'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)
    for keyword in keywords.keywords5:
        print(keyword)
        type = '세븐틴'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)
    for keyword in keywords.keywords6:
        print(keyword)
        type = '뉴이스트'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)
    for keyword in keywords.keywords7:
        print(keyword)
        type = '트와이스'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)
    for keyword in keywords.keywords8:
        print(keyword)
        type = '레드벨벳'
        press = 'SPOTV_NEWS'
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_MIDDLE + TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(1, url, type, press)