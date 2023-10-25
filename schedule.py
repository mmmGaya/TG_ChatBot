# import openpyxl

# group_number = input("Введите номер группы: ")
# excel_file_path = 'data/schedule/25.10.2023.xlsx'
# workbook = openpyxl.load_workbook(excel_file_path)
# print(workbook.sheetnames)

# # пары по номеру группы
# def get_schedule(group_number):
#     schedule = []
#     for sheet_name in workbook.sheetnames:
#         if sheet_name.startswith('Пара'):
#             sheet = workbook[sheet_name]
#             for row in sheet.iter_rows(min_row=2, values_only=True):
#                 if row[1] == group_number or row[4] == group_number:
#                     schedule.append({
#                         'Пара': sheet_name,
#                         'Аудитория': [row[0], row[3]],
#                         'Преподаватель': [row[2], row[5]]
#                     })
#     return schedule

# schedule = get_schedule(group_number)

# # вывод
# if schedule:
#     print(f"Расписание для группы {group_number}:")
#     for item in schedule:
#         print(f"{item['Пара']}: Аудитория {item['Аудитория']}, Преподаватель: {item['Преподаватель']}")
# else:
#     print(f"Расписание для группы {group_number} не найдено.")




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

url = 'https://rksi.ru/schedule'
r_post = requests.post(url, {'group': 'ИС-13', "stt": "Показать!"})
soup = BeautifulSoup(r_post.text, features="lxml")
lst = [i.get_text().strip() for i in soup.find_all(['p', 'b'])[2:-1]]
# print([i.get_text().strip() for i in soup.find_all(['b'])])

words_to_check = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']

# проверка каждого элемента в списке
filtered_lst = [item for item in lst if any(word in item for word in words_to_check)]

print(filtered_lst)



# исходник списка для теста
input_list = ['26 октября, четверг', '08:00  —  09:30МатематикаНаливайко Е.П., ауд. 322-1', 'Математика']

# распределие информации
time = input_list[1].split(input_list[2])[0].strip()
obj = input_list[2]
teacher = input_list[1].split(input_list[2])[1].strip().split(', ауд. ')[0]
aud = input_list[1].split(input_list[2])[1].strip().split(', ауд. ')[1]

# результат
print("Время:", time)
print("Предмет:", obj)
print("ФИО преподавателя:", teacher)
print("Аудитория:", aud)