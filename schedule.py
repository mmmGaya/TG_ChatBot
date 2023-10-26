import requests
import re
from bs4 import BeautifulSoup

url = 'https://rksi.ru/schedule'

r_post = requests.post(url, {'group': 'ИС-34', "stt": "Показать!"})
soup = BeautifulSoup(r_post.text, features="lxml")

rasp_row = soup.find('main')
rasp_lst = rasp_row.find_all(['p', 'hr'])[2:]
rasp_lst = [str(i) for i in rasp_lst]
print(rasp_lst)

lst = [i.get_text() for i in soup.find_all(['p', 'b'])[2:-1]]

# нахождение и удаление даты из списка
words_to_check = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
date_lst = [item for item in lst if any(word in item for word in words_to_check)]

# регулярные выражения для разбиения строк
pattern1 = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (\d+-\d+)')
pattern2 = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (с/з\d+-\d+)')
pattern3 = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (\d+а-\d+)')

patterns = [pattern1, pattern2, pattern3]

for date in range(len(date_lst)):
    print('-'*5)
    print(date_lst[date])
    print('-'*5)
    # Перебираем каждый элемент списка и разбиваем его на дату, время, предмет и преподавателя
    for i, item in enumerate(rasp_lst):
        matched = False
        for pattern in patterns:
            match = pattern.search(item)
            if match:
                start_time, end_time, subject, teacher, classroom = match.groups()
                print(f"Время: {start_time} — {end_time}")
                print(f"Предмет: {subject}")
                print(f"Преподаватель: {teacher}")
                print(f"Аудитория: {classroom}", '\n')
                matched = True
                break
        if not matched: 
            del rasp_lst[0:i+1]
            break


# teachers = soup_rksi.find('select', id = 'teacher').find_all('option')
# teachers_list = []
# for i in teachers:
#   teachers_list.append(i.text)
# teachers_list
# r_post = requests.post(url, {'teacher': 'Барна Н.В.', "stp": "Показать!"})
# soup = BeautifulSoup(r_post.text, features="lxml")
# [i.get_text() for i in soup.find_all(['p','b'])[2:-1]]
