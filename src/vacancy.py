import requests
import json

from HeadHunterAPI import HeadHunterABC


url = 'https://api.hh.ru/vacancies'

class Vacancy:

    """Класс для работы с вакансиями"""

    name_vacancy: str
    city: str
    salary: float
    url: str
    def __init__(self, name_vacancy, city, salary_from, salary_to, url):
        self.name_vacancy = name_vacancy
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.__validate()


    def __validate(self):
        if not self.salary_from:
            self.salary_from = 0
        else:
            self.salary_from = self.salary_from
        if not self.salary_to:
            self.salary_to = 0
        else:
            self.salary_to = self.salary_to

    def to_json_date(self):
        data = {
            'name_vacancy': self.name_vacancy,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'city': self.city,
            'url': self.url
        }
        return data
    def __str__(self):
        pass

    @classmethod
    def create_objects_from_data(cls, data: list[dict]):
        for date_vacancy in data:
            init_data = {
                'name_vacancy': date_vacancy['name'],
                'city': date_vacancy['area']['name'],
                'url': date_vacancy['alternate_url']
            }
            if date_vacancy['salary']:
                init_data['salary_from'] = date_vacancy['salary']['from']
                init_data['salary_to'] = date_vacancy['salary']['to']
            else:
                init_data['salary_from'] = None
                init_data['salary_to'] = None
            instance = cls(**init_data)
            instances.append(instance)

    def get_api(self):
        """Подключение к API"""
        params = {'text': f'NAME:{self.name_vacancy}',
                  'city': f'{self.city}',
                  'salary': f'{self.salary}',
                  'experience': f'{self.url}'}
        response = requests.get(url, params = params)
        return response.json()


    def filter_vacancies(self):
        vacancies_list  = []
        filter_words
        for vacancy in
            if vacancy == filter_words





