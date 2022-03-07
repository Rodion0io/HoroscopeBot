import requests
import lxml
from bs4 import BeautifulSoup
import time
import schedule

url = 'https://horoscopes.rambler.ru/'
Dict = {}
D = {}
B = []
A = ['Овен','Телец','Близнецы','Рак','Лев','Дева','Весы','Скорпион','Стрелец','Козерог','Водолей','Рыбы']

# cобрал нужные кнопки и их ссылки
def parse():
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    all_znak = soup.find_all('a', class_='zj8qn')
    for i in all_znak[9:21]:
        i_text = i.text
        i_href = 'https://horoscopes.rambler.ru' + i.get('href')
        Dict[i_text] = i_href

# собрал нужные данные из каждых ссылок
    for urls in Dict.values():
        req_1 = requests.get(urls)
        soup_1 = BeautifulSoup(req_1.text, 'lxml')
        all_text_from_url = soup_1.find_all('p', class_='mtZOt')
        for j in all_text_from_url:
            a = j.text
            B.append(a)

# Объеденил название знаков с их гороскопами
    for x,y in zip(A,B):
        D[x] = y
    return D


# Установил таймер
# schedule.every().day.at("09:00").do(parse)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)