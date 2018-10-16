import re


# 클리닝 함수

def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    cleaned_text = re.sub('^\s+[0-9]+\s+[0-9]+\s+[0-9]*\s', '', cleaned_text)
    return cleaned_text
