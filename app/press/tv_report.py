import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

# TV리포트
from app import keywords, text_cleaner, db
from app.models import Article

TARGET_URL_BEFORE_KEYWORD = 'http://www.tvreport.co.kr/?c=news&m=search&q='

print('word_test24_start')


# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(URL):
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

        # 기사 본문 내용 긁어오기 (위 함수 내부에서 기사 본문 주소 받아 사용되는 함수)
        source_code_from_url = urllib.request.urlopen(title_link)
        soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
        content_of_article = soup.select('div#CmAdContent')
        print(content_of_article)
        # for item in content_of_article_title + content_of_article:
        for item in content_of_article:
            string = str(item.find_all(text=True))
            print(string)
            string_item = text_cleaner.clean_text(string)
            a = Article(title_name=title_link, body=string_item)
            db.session.add(a)
            db.session.commit()



# 메인함수
def main():

    for keyword in keywords.keywords1:
        print(keyword)
        k = keyword
        url = TARGET_URL_BEFORE_KEYWORD + quote(k)
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(url)
        # output_file.close()


# if __name__ == '__main__':
#     main(sys.argv)