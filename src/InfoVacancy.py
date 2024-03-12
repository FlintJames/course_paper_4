import os.path

from src.vacancy import Vacancy
from config import ROOT_DIR
import json
class InfoVacancy:
    """Класс для сохранения информации о вакансиях в JSON-файл"""
    def __init__(self, filename):
        self.FILE_PATH = os.path.join(ROOT_DIR, 'data', filename)
        self.__check_file_exists()

    def __check_file_exists(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w') as file:
                json.dump([], file)

    def __load_date(self):
        with open(self.FILE_PATH) as file:
            content: list = json.load(file)
        return content

    def __dump_data(self, content):
        with open(self.FILE_PATH, 'w') as file:
            json.dump(content, file, indent=4, ansure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy):
        date_vacancy = {
            'name_vacancy': vacancy.name_vacancy,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'city': vacancy.city,
            'url': vacancy.url
        }
        content = self.__load_date()
        content.append(date_vacancy)
        with open(self.FILE_PATH) as file:
            content: list = json.load(file)
        content.append(date_vacancy)
        with open(self.FILE_PATH, 'w') as file:
            json.dump(content, file, indent=4, ensore_ascii=False)

    def add_vacancies(self, vacancies: list[Vacancy]):
        vacancies_datas = []
        for vacancy in vacancies:
            date_vacancy = vacancy.to_json_date()
            vacancies_datas.append(date_vacancy)

        content = self.__load_date()
        content.extend(vacancies_datas)
        self.__dump_data(content)
