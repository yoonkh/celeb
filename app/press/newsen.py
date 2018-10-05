from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

from flask import session
from selenium import webdriver

# 스포츠동아
from app import keywords, db, text_cleaner
from app.models import Article
from app.press import tv_report

# TARGET_URL_BEFORE_BASE = "http://www.newsen.com"
# TARGET_URL_BEFORE_KEYWORD = '/news_list.php?vm=list&searchperiod=all&search=title&searchstring='
# TARGET_URL_REST = '&page='


# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(keyword, type, press):

    downloadDestination = 'http://www.newsen.com/'

    # dir = r'/etc/apt/sources.list.d/google.list'
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    driver.get(downloadDestination)

    # driver.find_element_by_xpath('//*[@id="header_tving"]/div[1]/div/div[4]/button').click()
    driver.find_element_by_xpath('//*[@id="search_form"]/input[2]').send_keys(keyword)
    driver.find_element_by_xpath('//*[@id="search_form"]/input[3]').click()
    # driver.find_element_by_name('kw').send_keys(keyword)
    # driver.find_element_by_xpath('//*[@id="search"]/fieldset/div/button').click()
    # driver.find_element_by_xpath('//*[@id="news_list"]/div[3]/span/a').click()


    for a in driver.find_elements_by_xpath(
            '/html/body/p/table/tbody/tr/td/table/tbody/tr/td[1]/p/table/tbody/tr/td/table[2]/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/a'):
        # print(a.get_attribute('href'))
            # print(i)
        url = a.get_attribute('href')
        print(url)
        str_url = str(url)
        source_code_from_url = urllib.request.urlopen(str_url)

        soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
        # print(soup)
        content_of_article = soup.select('div#CLtag')
        # print(content_of_article)
        # for item in content_of_article_title + content_of_article:
        for item in content_of_article:
            # print(item)
            string = str(item.find_all(text=True))
            string_item = text_cleaner.clean_text(string)
            article = Article(title_name=str_url, body=string_item, type=type, press=press)
            db.session.add(article)
            db.session.commit()
            print('#####################Success######################')

    # for i in range(page_num):
    #     current_page_num = 1 + i
    #     URL_with_page_num = URL + str(current_page_num)
    #     print(URL_with_page_num)
    #     source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
    #     soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    #     # print(soup)
    #     # print(soup.select('td > a.line'))
    #
    #     for title in soup.select('tr > td > a.line'):
    #         title_link = title['href']
    #         print(title_link)
    #         edit_title_link_keyword = title_link[1:65]
    #         print(edit_title_link_keyword)
    #         edit_title_link = TARGET_URL_BEFORE_BASE+edit_title_link_keyword+quote(type)
    #         # print(edit_title_link)
    #
    #         source_code_from_url = urllib.request.urlopen(edit_title_link)
    #         soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    #         # 동아일보 기사 제목도 함께 추출
    #         # content_of_article_title = soup.select('div.article_title > h2')
    #         content_of_article = soup.select('div#CLtag')
    #
    #         # for item in content_of_article_title + content_of_article:
    #         for item in content_of_article:
    #             string = str(item.find_all(text=True))
    #             print(string)
    #             string_item = text_cleaner.clean_text(string)
    #             a = Article(title_name=edit_title_link, body=string_item, type=type, press=press)
    #             db.session.add(a)
    #             db.session.commit()

# 메인함수
def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = '뉴스엔'
        k = keyword
        # url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        # get_link_from_news_title(k, type, press)
        get_link_from_news_title(k, type, press)

    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '방탄소년단'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)
    # for keyword in keywords.keywords3:
    #     print(keyword)
    #     type = '엑소'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)
    # for keyword in keywords.keywords4:
    #     print(keyword)
    #     type = '비투비'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)
    # for keyword in keywords.keywords5:
    #     print(keyword)
    #     type = '세븐틴'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)
    # for keyword in keywords.keywords6:
    #     print(keyword)
    #     type = '뉴이스트'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)
    # for keyword in keywords.keywords7:
    #     print(keyword)
    #     type = '트와이스'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)
    # for keyword in keywords.keywords8:
    #     print(keyword)
    #     type = '레드벨벳'
    #     press = '뉴스엔'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k, encoding='euc-kr') + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type, press)

# print('word_test_end')

#
# if __name__ == '__main__':
#     main()
# tv_report.main()