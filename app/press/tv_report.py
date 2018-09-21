import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import word_test

# TV리포트
from app import keywords

TARGET_URL_BEFORE_KEYWORD = 'http://www.tvreport.co.kr/?c=news&m=search&q='

print('word_test24_start')


# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(URL, output_file):
    # for i in range(page_num):
    # current_page_num = i
    # position = URL.index('r/')
    # print(position)
    # position2 = URL.index('&keyword=')
    URL_with_page_num = URL
    # print(URL_with_page_num)
    source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    # print(soup)
    for link in soup.select('div.sec_small.contbox > a'):
        title_link = TARGET_URL_BEFORE_KEYWORD[:25] + link['href']
        # print(a[0]['href'])
        # for title in soup.select('div.slist > dl > dd > a'):
        #     # print(title)
        #     title_link = title['href']
        #     print(title_link)
        get_text(title_link, output_file)


# 기사 본문 내용 긁어오기 (위 함수 내부에서 기사 본문 주소 받아 사용되는 함수)
def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div#CmAdContent')
    print(content_of_article)
    # for item in content_of_article_title + content_of_article:
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write('\n\n\n' + string_item)


# 메인함수
def main(argv):

    for keyword in keywords.keywords1:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords2:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('방탄소년단_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords3:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('엑소_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords4:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('비투비_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords5:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('세븐틴_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords6:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('뉴이스트_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords7:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('트와이스_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    for keyword in keywords.keywords8:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        output_file = open('레드벨벳_in.txt', 'a')
        get_link_from_news_title(url, output_file)
        output_file.close()
    print('word_test24_end')


if __name__ == '__main__':
    main(sys.argv)