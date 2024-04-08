import json


def getting_file(file_name):
    """Эта функция загружает и возвращает содержимое JSON-файла"""
    with open(file_name, "r") as load_file:
        return json.load(load_file)
