"""Перегоняем составляем нужные данные"""

import json
from openpyxl import Workbook


def  create_excel():
    description_vacansions = [] # составленое описани
    with open('vacansions.json', mode='r', encoding='utf-8') as f:
        data  = json.load(f)

    pages =  len(data)

    # вытаскиваем только нужные данные, остальное будет завистеть от запроса
    for page in range(pages):
        number_vacancieslen = len(data[page]['items'])  # тут количество вакансий
        for i in range(number_vacancieslen):
            vacantion = data[page]['items'][i]   # тут получается передается одна вакансия
            name = vacantion['name']            # название вакансии
            url = vacantion['alternate_url']    # url
            description = vacantion['snippet']['requirement']
            name_compani = vacantion['employer']['name']
            employment = vacantion['employment']['name']  # Занятость
            description_vacansions += [(name, description, url, name_compani, employment)]  # добавляет, все ок.

    # создание excel

    work_book = Workbook()  # запус exel
    sheet = work_book.active # это переключаемся на активный лист, первый
    sheet['A1'] = 'Просмотрено'
    sheet['B1'] = 'Вердикт'
    sheet['C1'] = 'Примечание'
    sheet['D1'] = 'Отправил отклик'
    sheet['E1'] = 'Ответ на отклик'
    sheet['F1'] = 'Вакансия'  # добавляем название для столбца на соединении A и 1
    sheet['G1'] = 'Компания'
    sheet['H1'] = 'Описание'
    sheet['I1'] = 'Адрес страницы'
    sheet['J1'] = 'Занятость'
    # а вот тут наверное будет цикл чтобы добавить так как это не меняется
    for name, desc, url, name_comp, emp in description_vacansions:
        sheet.append(['нет','','','нет','',name, name_comp ,desc, url, emp])  # Заполняем строки, типо желательно чтобы совпадали

    work_book.save("вакансии.xlsx")  # Сохраняем
