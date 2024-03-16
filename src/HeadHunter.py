from abc import ABC, abstractmethod

import requests


class BaseAPI(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""
    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunter(BaseAPI):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'per_page': 10,
            'area': 113
        }

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        response = requests.get(self.url, params=self.params)
        data = response.json()
        if response.status_code == 200:
            return data['items']
        else:
            print("Произошла ошибка")

