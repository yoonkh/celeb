import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

from app import text_cleaner, db, keywords
from app.models import Article


TARGET_URL_BEFORE_KEYWORD = 'http://star.mt.co.kr/search/index.html?srchFd=TOTAL&range=TOTAL&reSrchFlag=&preKwd=&search_type=s&' \
                            'kwd='
TARGET_URL_BEFORE_PAGE_NUM = '&detailYN=0&bgndt=&enddt=&category=STNW&sortType=allwordsyn&subYear=&subType=' \
                             '&pageNum='



# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, type, press):

    for i in range(page_num):
        current_page_num = 1 + i
        URL_with_page_num = URL + str(current_page_num)
        # print(URL_with_page_num)
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'html5lib', from_encoding='utf-8')
        # print(soup)
        # print(soup.find_all('div', 'section_list_text'))
        for title in soup.select('strong.tit > a'):
            # print(title)
            article_URL = title['href']
            # print(article_URL)
            source_code_from_url = urllib.request.urlopen(article_URL)
            soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')

            # 동아일보 기사 제목도 함께 추출
            # content_of_article_title = soup.select('div.article_title > h2')
            content_of_article = soup.select('div.article')

            # for item in content_of_article_title + content_of_article:
            for item in content_of_article:
                string = str(item.find_all(text=True))
                print(string)
                string_item = text_cleaner.clean_text(string)
                a = Article(title_name=article_URL, body=string_item, type=type, press=press)
                db.session.add(a)
                db.session.commit()



def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords3:
        print(keyword)
        type = '엑소'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords4:
        print(keyword)
        type = '비투비'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords5:
        print(keyword)
        type = '세븐틴'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords6:
        print(keyword)
        type = '뉴이스트'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords7:
        print(keyword)
        type = '트와이스'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords8:
        print(keyword)
        type = '레드벨벳'
        press = '스타뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_BEFORE_PAGE_NUM
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)