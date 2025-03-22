# source venv_parse_hh/Scripts/activate
"""Прога просто создает много файлов с вакансиями"""

import requests
import json
import time

# url = 'https://api.hh.ru/vacancies?text=python&page=100&per_page=M'

def parse(*,vacantion, pages, per_page):
    url_base = 'https://api.hh.ru/vacancies?' #  рабочий url

    list_jobs = []  # переменная для хранения всех работ

    for page in range(pages):
        response = requests.get(url=f'{url_base}text={vacantion}&page={page}&per_page={per_page}')
        if response.ok:
            list_jobs += [response.json()]
            time.sleep(5)
        else:
            print(response.status_code)
            break

    with open('vacansions.json', 'w', encoding='utf-8') as f:
        json.dump(list_jobs, f)
