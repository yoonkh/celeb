import re

# 입,출력 파일명
INPUT_FILE_NAME = ['워너원_in.txt', '방탄소년단_in.txt', '엑소_in.txt', '비투비_in.txt', '세븐틴_in.txt', '뉴이스트_in.txt', '트와이스_in.txt', '레드벨벳_in.txt']

# OUTPUT_FILE_NAME = 'output_cleaned.txt'
OUTPUT_FIlE_NAME = ['워너원_out.txt', '방탄소년단_out.txt', '엑소_out.txt', '비투비_out.txt', '세븐틴_out.txt', '뉴이스트_out.txt', '트와이스_out.txt', '레드벨벳_out.txt']

# 클리닝 함수
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    return cleaned_text
