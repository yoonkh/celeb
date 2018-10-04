from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

# 스포츠동아
from app import keywords, db, text_cleaner
from app.models import Article
from app.press import tv_report

TARGET_URL_BEFORE_BASE = "http://joynews.inews24.com"
TARGET_URL_BEFORE_KEYWORD = '/search/?word='
TARGET_URL_REST = '&period=all&sort=new&tab=news&sec=tc&s_date=&e_date=&page='

# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, type, press):
        for i in range(page_num):
            current_page_num = 1 + i
            # position = URL.index('&page=')
            URL_with_page_num = URL + str(current_page_num)
            print(URL_with_page_num)
            source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
            soup = BeautifulSoup(source_code_from_URL, 'lxml',
                                 from_encoding='utf-8')
            for title in soup.find_all('li', 'list'):
                title_link = title.select('a')
                article_URL = title_link[0]['href']
                article_URL = TARGET_URL_BEFORE_BASE + article_URL
                print(article_URL)


                source_code_from_url = urllib.request.urlopen(article_URL)
                soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
                # content_of_article_title = soup.select('div.article_title > h2')
                content_of_article = soup.select('article#articleBody')
                # print(content_of_article)
                # for item in content_of_article_title + content_of_article:
                for item in content_of_article:
                    string = str(item.find_all(text=True))
                    print(string)
                    string_item = text_cleaner.clean_text(string)
                    a = Article(title_name=article_URL, body=string_item, type=type, press=press)
                    db.session.add(a)
                    db.session.commit()
                    # output_file.write('\n\n\n' + string_item)


# 메인함수
def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)

    for keyword in keywords.keywords2:
        print(keyword)
        type = '방탄소년단'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords3:
        print(keyword)
        type = '엑소'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords4:
        print(keyword)
        type = '비투비'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords5:
        print(keyword)
        type = '세븐틴'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords6:
        print(keyword)
        type = '뉴이스트'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords7:
        print(keyword)
        type = '트와이스'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)
    for keyword in keywords.keywords8:
        print(keyword)
        type = '레드벨벳'
        press = '조이뉴스'
        k = keyword
        url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(3, url, type, press)

# print('word_test_end')

#
# if __name__ == '__main__':
#     main()
# tv_report.main()