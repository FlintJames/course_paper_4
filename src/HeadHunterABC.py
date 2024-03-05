from abc import ABC, abstractmethod


class HeadHunterABC(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""
    @abstractmethod
    def get_api(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def delete_date(self):
        pass
