import json


def getting_file(file_name):
    """Эта функция загружает и возвращает содержимое JSON-файла"""
    with open(file_name, "r") as load_file:
        return json.load(load_file)


def filtration_list(load_file):
    """Эта функция отсеивает пустые строки и оставляет значения ключа равное 'EXECUTED'"""
    json_file = list(filter(lambda x: len(x) and x['state'] == 'EXECUTED', load_file))
    return json_file
