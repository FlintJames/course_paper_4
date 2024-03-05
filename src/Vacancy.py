from HeadHunterABC import HeadHunterABC


class Vacancy(HeadHunterABC):

    """Класс для работы с вакансиями"""

    name_vacancy: str
    link_vacancy: str
    salary: float
    requirements: str
    def __init__(self, name_vacancy, link_vacancy, salary, requirements):
        self.name_vacancy = name_vacancy
        self.link_vacancy = link_vacancy
        self.salary = salary
        self.requirements = requirements

    def get_api(self):
        """Подключение к API"""
        pass

    def compare_salary(self):
        """Сравнение заработной платы у вакансий"""

        if salary in salary == None:
            return f'Зарплата не указана'
        else:
            return f'{}'


