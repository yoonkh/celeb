import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

# 스포츠동아
import keywords
import word_test24

TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEYWORD = '&query='
TARGET_URL_REST = '&check_news=6&more=1&sorting=1&search_date=1&v1=&v2=&range=1'


print('word_test_start')


# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, output_file):
    try:
        for i in range(page_num):
            current_page_num = 1 + i * 15
            position = URL.index('=')
            URL_with_page_num = URL[: position + 1] + str(current_page_num) \
                                + URL[position + 1:]
            # print(URL_with_page_num)
            source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
            soup = BeautifulSoup(source_code_from_URL, 'lxml',
                                 from_encoding='utf-8')
            for title in soup.find_all('p', 'tit'):
                title_link = title.select('a')
                article_URL = title_link[0]['href']
                get_text(article_URL, output_file)
    except Exception:
        pass


# 기사 본문 내용 긁어오기 (위 함수 내부에서 기사 본문 주소 받아 사용되는 함수)
def get_text(URL, output_file):
    try:
        source_code_from_url = urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
        # 동아일보 기사 제목도 함께 추출
        # content_of_article_title = soup.select('div.article_title > h2')
        content_of_article = soup.select('div.article_txt')
        print(content_of_article)

        # for item in content_of_article_title + content_of_article:
        for item in content_of_article:
            string_item = str(item.find_all(text=True))
            output_file.write('\n\n\n' + string_item)
    except Exception:
        pass

# 메인함수
def main():

    for keyword in keywords.keywords1:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords2:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('방탄소년단_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords3:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('엑소_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords4:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('비투비_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords5:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('세븐틴_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords6:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('뉴이스트_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords7:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('트와이스_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()
    for keyword in keywords.keywords8:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        output_file = open('레드벨벳_in.txt', 'a')
        get_link_from_news_title(3, url, output_file)
        output_file.close()

print('word_test_end')

if __name__ == '__main__':
    main()
    word_test24.main()