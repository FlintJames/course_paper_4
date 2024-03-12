from abc import ABC

from coverage import data

from src import vacancy
from src.HeadHunter import BaseAPI, HeadHunter
from src.vacancy import Vacancy
from src.user import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().strip()
    salary_range = input("Введите диапазон зарплат (пример: 100000-150000): ")

    hh_api = HeadHunter()
    hh_vacancies = hh_api.get_vacancies(search_query)

    if hh_vacancies and 'items' in hh_vacancies:
        vacancies_list = [Vacancy(vacancy['name'], vacancy['alternate_url'],
                                  vacancy.get('salary', {}).get('from', 'Зарплата не указана'))]
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)

    print(hh_vacancies)



if __name__ == "__main__":
    user_interaction()
