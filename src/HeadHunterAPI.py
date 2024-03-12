from abc import ABC, abstractmethod

import requests


class API(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""
    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunterABC(API):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'per_page': 100,
            'area': 113
        }

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        response = requests.get(self.url, params=self.params)
        data = response.json()
        return data['items']


