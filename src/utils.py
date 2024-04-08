import json
from datetime import datetime


def getting_file(file_name):
    """Эта функция загружает и возвращает содержимое JSON-файла"""
    with open(file_name, "r") as load_file:
        return json.load(load_file)


def filtration_list(load_file):
    """Эта функция отсеивает пустые строки и оставляет значения ключа равное 'EXECUTED'"""
    json_file = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_file


def sorted_date(json_file):
    """Эта функция сортирует список словарей в убывающем порядке дат, преобразованных в необходимый формат"""
    json_sort = sorted(json_file,key=lambda x: datetime.strptime(x['date'],'%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort
