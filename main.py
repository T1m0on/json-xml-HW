import json
import xmltodict
from collections import Counter



def get_news_json(file):
    with open(file, encoding='utf-8') as f:
        news = json.load(f)
    return news


def get_news_xml(file):
    with open(file, encoding="utf-8") as f:
        news = xmltodict.parse(f.read())
        return news


def get_words(file_data, item_key):
    all_words = []
    for news in file_data['rss']['channel'][item_key]:
        words = news['title'] + news['description']
        for word in words.split():
            if len(word) > 6:
                all_words += word.split()
    res = Counter(all_words).most_common(10)
    print(res)

def get_any_news():
    item_key = ''
    while item_key != '0':
        item_key = input('Какой файл читаем? \n1)newsafr.json \n2)newsafr.xml \n0)Выход \n')
        if item_key == '1':
            file = 'newsafr.json'
            item_key = 'items'
            file = get_news_json(file)
            get_words(file, item_key)
        elif item_key == '2':
            file = 'newsafr.xml'
            item_key = 'item'
            file = get_news_xml(file)
            get_words(file, item_key)
        else:
            print('Две таблетки, одна синяя, другая красная, третьего не дано')

get_any_news()





