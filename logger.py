import os
from data_create import name_data, surname_data, phone_data, adress_data

file_name = 'data.txt'


def print_data():
    if os.path.exists(file_name):
        print('Вывод данных из файла')
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines()  # возвращает все строки
            for element in list_data:
                print(element)
    else:
        print("Файл не существует")


def input_data():
    print('Введите данные для записи в файл')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{name}; {surname}; {phone}; {adress}\n")


def filter_data():
    filter_string = input()
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        if ";" in filter_string:
            list_filter = filter_string.split(";")
        else:
            list_filter = [filter_string]
        match = 0
        # if(accurate_filter(list_data, list_filter)) > 1:
        #     print("hdjghdjghfdh")
        #     accurate_filter(list_data, list_filter)
        for j in range(len(list_data)):
            count = 0
            for i in list_filter:
                if i in list_data[j]:
                    count += 1
            if count == len(list_filter):
                print(f"[{j}] {list_data[j]}")
                match += 1
        if match == 0:
            print("Записей не найдено") 
        elif match > 1:
            print(f"Найдено {match} записи")        

# def accurate_filter(list_data, list_filter):
#     match = 0
#     for j in range(len(list_data)):
#             count = 0
#             for i in list_filter:
#                 if i in list_data[j]:
#                     count += 1
#             if count == len(list_filter):
#                 print(f"[{j}] {list_data[j]}")
#                 match += 1
#     if match == 0:
#         print("Записей не найдено") 
#     elif match > 1:
#         print(f"Найдено {match} записи") 
#     return match

def change_data():
    delete_data()
    input_data()


def delete_data():
    filter_data()
    print("Для удаления элемента введите его номер (указан в квадратных скобках)")
    delete_elem = int(input())

    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        with open(file_name, 'w', encoding='utf-8') as fw:
            for j in range(len(list_data)):
                if j != delete_elem:
                    fw.write(list_data[j])
    print("Элемент удален!")
