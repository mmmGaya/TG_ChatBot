import requests
import re
from bs4 import BeautifulSoup

def get_group_schedule(group):
    url = 'https://rksi.ru/schedule'

    r_post = requests.post(url, {'group': 'ИС-34', "stt": "Показать!"})
    soup = BeautifulSoup(r_post.text, features="lxml")

    rasp_row = soup.find('main')
    rasp_lst = rasp_row.find_all(['p', 'hr'])[2:]
    rasp_lst = [str(i) for i in rasp_lst]

    lst = [i.get_text() for i in soup.find_all(['p', 'b'])[2:-1]]
    
    result = separation_text(lst=lst, rasp_lst=rasp_lst)
    return result


def get_teacher_schedule(teacher):
    url = 'https://rksi.ru/schedule'

    r_post = requests.post(url, {'teacher': teacher, "stp": "Показать!"})
    soup = BeautifulSoup(r_post.text, features="lxml")

    rasp_row = soup.find('main')
    rasp_lst = rasp_row.find_all(['p', 'hr'])[2:]
    rasp_lst = [str(i) for i in rasp_lst]

    lst = [i.get_text() for i in soup.find_all(['p', 'b'])[2:-1]]

    result = separation_text(lst=lst, rasp_lst=rasp_lst)
    return result


def separation_text(lst, rasp_lst):
    # нахождение и удаление даты из списка
    words_to_check = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
    date_lst = [item for item in lst if any(word in item for word in words_to_check)]

    # регулярные выражения для разбиения строк
    pattern1 = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (\d+-\d+)')
    pattern2 = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (с/з\d+-\d+)')
    pattern3 = re.compile(r'(\d{2}:\d{2})\s+—\s+(\d{2}:\d{2})<br/><b>(.+?)</b><br/>(.+?), ауд\. (\d+а-\d+)')

    patterns = [pattern1, pattern2, pattern3]
    result = []

    for date in range(len(date_lst)):
        day_schedule = []
        day_schedule.append(date_lst[date])
        # Перебираем каждый элемент списка и разбиваем его на дату, время, предмет и преподавателя
        for i, item in enumerate(rasp_lst):
            matched = False
            for pattern in patterns:
                match = pattern.search(item)
                if match:
                    start_time, end_time, subject, people, classroom = match.groups()
                    day_schedule.append({
                        'Время': f"{start_time} — {end_time}",
                        'Предмет': subject,
                        'Общность': people,
                        'Аудитория': classroom
                    })
                    matched = True
                    break
            if not matched: 
                del rasp_lst[0:i+1]
                break
        result.append(day_schedule)
    return result


# Пример использования функции для получения расписания группы
group_schedule = get_group_schedule(input('Введите номер группы: ').upper())
# for day_schedule in group_schedule:
#     print('—' * 10)
#     print('📅', day_schedule[0])
#     print('—' * 10)

#     for lesson in day_schedule[1:]:
#         print(f"⏳: {lesson['Время']}")
#         print(f"📒: {lesson['Предмет']}")
#         print(f"🎓: {lesson['Общность']}")
#         print(f"🔑: {lesson['Аудитория']}", '\n')


# Пример использования функции для получения расписания преподавателя (Каламбет В.Б.)
# group_schedule = get_teacher_schedule(input('Введите ФИО преподавателя: ').title())
# for day_schedule in group_schedule:
#     print('—' * 10)
#     print('📅', day_schedule[0])
#     print('—' * 10)

#     for lesson in day_schedule[1:]:
#         print(f"⏳: {lesson['Время']}")
#         print(f"📒: {lesson['Предмет']}")
#         print(f"🎓: {lesson['Общность']}")
#         print(f"🔑: {lesson['Аудитория']}", '\n')
