import os
from data_create import name_data, surname_data, phone_data, adress_data

file_name = 'data.txt'

def print_data():
    if os.path.exists(file_name):
        print('Вывод данных из файла')
        with open(file_name, 'r', encoding='utf-8') as file:
            list_data = file.readlines() # возвращает все строки
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
        # print(list_data)
        if ";" in filter_string:
            list_filter = filter_string.split(";")
        else:
            list_filter = [filter_string]

        is_found = False
        count_2 = 0
        for element in list_data:
            temp_record = element.split(";")
            # print(temp_record)
            count = 0
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower(): #and len(element_filter.lower()) == len(record.lower()):
                        count += 1
                        # print(count, record)
            if count >= len(list_filter):
                print(element)
                count_2 += 1
                is_found = True
            # print(count_2)
    if not is_found:
        print("Записей не найдено")
    else:
        if count_2 > 1: 
            lit = "о"
            lit_2 = "а"
        else:
            lit = ""
            lit_2 = ""
        print(f'Найден{lit} {count_2} элемент{lit_2}')
                
def change_data ():
    filter_data()
    
    print('5+')

def delete_data():
    filter_string = input()
    with open(file_name, 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        # print(list_data)
        if ";" in filter_string:
            list_filter = filter_string.split(";")
        else:
            list_filter = [filter_string]

        is_found = False
        count_2 = 0
        for element in list_data:
            temp_record = element.split(";")
            # print(temp_record)
            count = 0
            for record in temp_record:
                for element_filter in list_filter:
                    if element_filter.lower() in record.lower(): #and len(element_filter.lower()) == len(record.lower()):
                        count += 1
                        print(count, record)
            if count >= len(list_filter):
                print(element)
                count_2 += 1
                is_found = True
            # print(count_2)
    if not is_found:
        print("Записей не найдено")
    else:
        if count_2 > 1: 
            lit = "о"
            lit_2 = "а"
        else:
            lit = ""
            lit_2 = ""
        print(f'Найден{lit} {count_2} элемент{lit_2}')
    if count_2 > 1:
        print('Уточните параметры')
        delete_data()
    d = str(input('Удалить этот элемент "Д/Н" ?'))
    if d.lower() == "д":
        print(temp_record, element, record)
        # temp_record.clear()