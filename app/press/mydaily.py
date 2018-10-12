import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

from app import text_cleaner, db, keywords
from app.models import Article

TARGET_URL_BEFORE_MAIN = 'http://www.mydaily.co.kr/new_yk/html'
TARGET_URL_BEFORE_KEYWORD = '/search_mj.php?search='
TARGET_URL_BEFORE_PAGE = '&listpg='


# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, type, press):
    for i in range(page_num):
        current_page_num = 1 + i
        URL_with_page_num = URL + str(current_page_num)
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for title in soup.find_all('div', 'section_list_text'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            edit_title_URL = TARGET_URL_BEFORE_MAIN + article_URL[1:]
            # print(edit_title_URL)

            source_code_from_url = urllib.request.urlopen(edit_title_URL)
            soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
            content_of_article = soup.select('div.read_view_wrap > dd')

            title_item = soup.select('div.read_view_wrap')[0].find_all('dt')
            print(title_item)

            tit = ""

            for t in title_item:
                string = str(t.find_all(text=True))
                tit = text_cleaner.clean_text(string)

            for item in content_of_article:
                string = str(item.find_all(text=True))
                print(string)
                string_item = text_cleaner.clean_text(string)
                a = Article(title_name=tit, title_link=edit_title_URL, body=string_item, type=type, press=press)
                db.session.add(a)
                db.session.commit()



def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)

    for keyword in keywords.keywords3:
        print(keyword)
        type = '엑소'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords4:
        print(keyword)
        type = '비투비'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords5:
        print(keyword)
        type = '세븐틴'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords6:
        print(keyword)
        type = '뉴이스트'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords7:
        print(keyword)
        type = '트와이스'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords8:
        print(keyword)
        type = '레드벨벳'
        press = '마이데일리'
        k = keyword
        url = TARGET_URL_BEFORE_MAIN + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_BEFORE_PAGE
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)