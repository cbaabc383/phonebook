from logger import input_data, print_data, filter_data, change_data, delete_data

def interface():
    print("""Выберите режим работы: 
    1 - запись данных
    2 - вывод данных
    3 - поиск данных
    4 - изменение данных
    5 - удаление данных
    """)
    command = int(input("Введите номер команды: "))
    while command < 1 or command > 5:
        print("Ввеедите корректный номер команды")
        command = int(input("Введите номер команды: "))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        print('Введите параметры поиска через ";": ')
        filter_data()
    elif command == 4:
        print('Введите параметры изменяемой строки через ";":')
        # filter_string = input()
        change_data()
    elif command == 5:
        print('Введите параметры удаляемой строки через ";":')
        delete_data()