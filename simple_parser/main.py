import requests
from bs4 import BeautifulSoup
import pandas as pd

from funcs import parse_table


bank_id = 1771062
page = 1
max_page = 10
url = 'https://www.banki.ru/services/questions-answers/?id=%d&p=%d' % (bank_id, page)
result = pd.DataFrame()


# Отправляем HTTP запрос и получаем результат
r = requests.get(url) 
# Отправляем полученную страницу в библиотеку для парсинга
soup = BeautifulSoup(r.text) 
# Получаем все таблицы с вопросами
tables = soup.find_all('table', {'class': 'qaBlock'}) 
for item in tables:
    res = parse_table(item)
    result = result.append(res, ignore_index=True)


result.to_excel('result.xlsx')

# with open('test.html', 'w') as output_file:
# output_file.write(r.text)
