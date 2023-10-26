import requests
from bs4 import BeautifulSoup
# res = requests.get(url)
# soup_rksi = BeautifulSoup(res.text)
# teachers = soup_rksi.find('select', id = 'teacher').find_all('option')
# teachers_list = []
# for i in teachers:
#   teachers_list.append(i.text)
# teachers_list
# r_post = requests.post(url, {'teacher': 'Барна Н.В.', "stp": "Показать!"})
# soup = BeautifulSoup(r_post.text, features="lxml")
# [i.get_text() for i in soup.find_all(['p','b'])[2:-1]]

# -------------------------------------------------------------------------------
url = 'https://rksi.ru/schedule'

r_post = requests.post(url, {'group': 'ИС-13', "stt": "Показать!"})
soup = BeautifulSoup(r_post.text, features="lxml")

rasp_row = soup.find('main')
rasp_list1 = [i.get_text() for i in rasp_row.find_all(['p', 'hr'])[2:-1]]
print(rasp_list1)

lst = [i.get_text() for i in soup.find_all(['p', 'b'])[2:-1]]

# нахождение и удаление даты из списка
words_to_check = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
date_lst = [item for item in lst if any(word in item for word in words_to_check)]

# -----------------------------------------------------------------------------------

# print(filters_lst)

# for i, d in enumerate(filters_lst):
#     lst.remove(d)

# # исходник списка для теста
# # input_list = ['08:00  —  09:30МатематикаНаливайко Е.П., ауд. 322-1', 'Математика']
# for i in range(len(lst)):
#     # распределие информации
#     time = lst[i].split(lst[i+1])[0].strip()
#     obj = lst[i+1]
#     teacher = lst[i].split(lst[i+1])[1].strip().split(', ауд. ')[0]
#     aud = lst[i].split(lst[i+1])[1].strip().split(', ауд. ')[1]
#     # результат
#     print("Время:", time)
#     print("Предмет:", obj)
#     print("ФИО преподавателя:", teacher)
#     print("Аудитория:", aud)

#     lst.pop(i+1)


# --------------------------------
import re

# Исходный список
lst = ['<p>08:00  —  09:30<br/><b>Математика</b><br/>Наливайко Е.П., ауд. 322-1</p>', 
       '<p>09:40  —  11:10<br/><b>Физика</b><br/>Троилина В.С., ауд. 103-1</p>', 
       '<p>11:30  —  13:00<br/><b>Иностранный язык</b><br/>Ужегова  Е.А., ауд. 307-1</p>', 
       '<p>11:30  —  13:00<br/><b>Иностранный язык</b><br/>Прыгунова Т.А., ауд. 320-1</p>', '<hr/>',
       '<p>08:00  —  09:30<br/><b>МатемААААтика</b><br/>Наливайко Е.П., ауд. 322-1</p>', 
       '<p>09:40  —  11:10<br/><b>ФИИИИзика</b><br/>Троилина В.С., ауд. 103-1</p>', 
       '<p>11:30  —  13:00<br/><b>ИностраААААнный язык</b><br/>Ужегова  Е.А., ауд. 307-1</p>', 
       '<p>11:30  —  13:00<br/><b>ИностраААААнный язык</b><br/>Прыгунова Т.А., ауд. 320-1</p>', '<hr/>', 
       '<p>08:00  —  09:30<br/><b>AAAAAAAAAAAAAAAA</b><br/>Наливайко Е.П., ауд. 322-1</p>', 
       '<p>09:40  —  11:10<br/><b>FFFFFFFFFFFFFFFF</b><br/>Троилина В.С., ауд. 103-1</p>', 
       '<p>11:30  —  13:00<br/><b>AAAAAAAAAAAAAAA AAAA</b><br/>Ужегова  Е.А., ауд. 307-1</p>', 
       '<p>11:30  —  13:00<br/><b>aaaaaaaaaaaaaaa AAAA</b><br/>Прыгунова Т.А., ауд. 320-1</p>', 
]
# lst = ['08:00  —  09:30МатематикаНаливайко Е.П., ауд. 322-1', 
#        '09:40  —  11:10ФизикаТроилина В.С., ауд. 103-1', 
#        '11:30  —  13:00Иностранный языкУжегова  Е.А., ауд. 307-1', 
#        '11:30  —  13:00Иностранный языкПрыгунова Т.А., ауд. 320-1', '', 
#        '08:00  —  09:30ИнформатикаНаливайко Е.П., ауд. 322-1', 
#        '09:40  —  11:10МатематикаНаливайко Е.П., ауд. 322-1', 
#        '11:30  —  13:00ИсторияУпорова Л.В., ауд. 410-1', '', 
#        '08:00  —  09:30ИсторияУпорова Л.В., ауд. 410-1', 
#        '09:40  —  11:10МатематикаНаливайко Е.П., ауд. 322-1']

# Регулярные выражения для разбиения строк
pattern = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (\d+-\d+)')
# pattern = re.compile(r'(\d{2}:\d{2})\s*—\s*(\d{2}:\d{2})([А-Я][а-я]+)\s*([А-Я].*),\s*ауд\.\s*(\d+-\d+)')


# data_lst = ['26 октября, четверг', '27 октября, пятница', '28 октября, суббота']

for date in range(len(date_lst)):
    print(date_lst[date])
    # Перебираем каждый элемент списка и разбиваем его на дату, время, предмет и преподавателя
    for i, item in enumerate(lst):
        match = pattern.search(item)
        if match:
            start_time, end_time, subject, teacher, classroom = match.groups()

            print(f"Время: {start_time} - {end_time}")
            print(f"Предмет: {subject}")
            print(f"Преподаватель: {teacher}")
            print(f"Аудитория: {classroom}")
            print('---')
        else:
            del lst[0:i+1]
            break