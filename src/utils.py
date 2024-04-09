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
    json_sort = sorted(json_file, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return json_sort


def get_date(date):
    """Эта функция преобразует дату в короткий вид"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


def get_num(num):
    """Эта функция обрабатывает строку с информацией о номере счета или карты, скрывая часть цифр."""
    reg = num.split()
    if reg[0] == "Счет":
        return 'Счет **' + num[-4:]
    else:
        card_name = " ".join(reg[:-1])
        return card_name + ' ' + reg[-1][:4] + ' ' + reg[-1][4:6] + '** **** ' + reg[-1][-4:]


def get_sum(cash):
    """Эта функция возвращает сумму и наименование валюты из словаря"""
    return f'{cash["operationAmount"]["amount"]} {cash["operationAmount"]["currency"]["name"]}'


def get_main(num_operations=5):
    sorted_file = sorted_date(filtration_list( getting_file("operations.json")))
    for operation in sorted_file:
        if num_operations == 0:
            break
        print(get_date(operation["date"]), operation["description"])
        if operation["description"] != "Открытие вклада":
            print(get_num(operation["from"]) + " -> ", end="")
        print(get_num(operation["to"]))
        print(get_sum(operation),"\n")
        num_operations -= 1
