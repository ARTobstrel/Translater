import requests
import os

API_KEY = os.getenv('API_YANDEX')
url_translate = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
url_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'


def detect_lan(text):
    params = {'key': API_KEY,
              'text': text,
              'hint': 'ru,en'}
    res = requests.get(url_detect, params=params)
    if res.status_code == 200:
        res = res.json()
        if res['lang'] == 'en':
            return 'en-ru'
        if res['lang'] == 'ru':
            return 'ru-en'
    else:
        return 'Invalid KEY_API'


def translate_text(text, lan):
    params = {'key': API_KEY,
              'lang': lan,
              'text': text}
    res = requests.get(url_translate, params=params).json()
    return res['text'][0]


if __name__ == '__main__':
    text = input('Enter something: ')
    lan = detect_lan(text)
    try:
        print(translate_text(text, lan))
    except:
        print(lan)
