import requests
import json

from HeadHunterABC import HeadHunterABC


url = 'https://api.hh.ru/vacancies'

class Vacancy(HeadHunterABC):

    """Класс для работы с вакансиями"""

    name_vacancy: str
    city: str
    salary: float
    experience: str
    def __init__(self, name_vacancy, city, salary, experience):
        self.name_vacancy = name_vacancy
        self.city = city
        self.salary = salary
        self.experience = experience

    def get_api(self):
        """Подключение к API"""
        params = {'text': f'NAME:{self.name_vacancy}',
                  'city': f'{self.city}',
                  'salary': f'{self.salary}',
                  'experience': f'{self.experience}'}
        response = requests.get(url, params = params)
        return response.json()

    def add_vacancy(self):
        with open('vacancy.json', encoding='utf-8') as json_file:
            date_list = json.load(json_file)
        with open('vacancy.json', 'w', encoding='utf-8') as json_file:
            json.dump(date_list, json_file)


    def delete_date(self):
        with open('vacancy.json', 'r+', encoding='utf-8') as json_file:
            date_list = json.load(json_file)
            try:
                if vacancy in date_list:
                    del vacancy
            except ValueError:
                print('Вакансия не найдена')


    def filter_vacancies(self):
        vacancies_list  = []
        filter_words
        for vacancy in
            if vacancy == filter_words


    def compare_salary(self, all_vacancy):
        """Сравнение заработной платы у вакансий"""

        for vacancy in all_vacancy:
            if vacancy['salary'] is None:
                return f'Зарплата не указана'
            else:
                return f'{}'


