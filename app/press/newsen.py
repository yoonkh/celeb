from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
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
            '/html/body/p/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/a'):
        # print(a.get_attribute('href'))
        url = a.get_attribute('href')
        str_url = str(url)
        print(str_url)

        source_code_from_url = urllib.request.urlopen(str_url)
        soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
        print(soup)
        content_of_article = soup.select('div#CLtag')
        print(content_of_article)
        # for item in content_of_article_title + content_of_article:
        for item in content_of_article:
            # print(item)
            string = str(item.find_all(text=True))
            string_item = text_cleaner.clean_text(string)
            a = Article(title_name=str_url, body=string_item, type=type, press=press)
            db.session.add(a)
            db.session.commit()
            print('#####################Success######################')


# 메인함수
def main():

    for keyword in keywords.keywords1:
        print(keyword)
        type = '워너원'
        press = '뉴스엔'
        k = keyword
        # url = TARGET_URL_BEFORE_BASE + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
        # output_file = open('워너원_in.txt', 'a')
        get_link_from_news_title(k, type, press)

    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '방탄소년단'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)
    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '엑소'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)
    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '비투비'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)
    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '세븐틴'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)
    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '뉴이스트'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)
    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '트와이스'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)
    # for keyword in keywords.keywords2:
    #     print(keyword)
    #     type = '레드벨벳'
    #     k = keyword
    #     url = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEYWORD + quote(k) + TARGET_URL_REST
    #     # output_file = open('워너원_in.txt', 'a')
    #     get_link_from_news_title(3, url, type)

# print('word_test_end')

#
# if __name__ == '__main__':
#     main()
# tv_report.main()