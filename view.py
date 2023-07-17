def input_num():
    ask = int(input("Выберите действие:\n1 - Записать нового пользователя\n2 - Поиск пользователя\n3 - Изменить данные\n4 - Удалить данные\n5 - Сортировка\n6 - Вывести всех пользователей\n7 - выйти\n"))
    return ask

def input_name():
    id = input("Введите ID пользователя: ")
    name = input("Введите ФИО пользователя: ")
    phone = input("Введите номер пользователя: ")
    data = id + ", " + name + ", " + phone + "\n"
    return data

def input_found():
    f_file = input("Введите данные для поиска: ")
    return f_file

def input_change():
    ch = input("Введите данные, которые хотите изменить: ")
    return ch

def input_choice():
    option = int(input("Как вы хотите изменить данные:\n1 - частично(только указанные данные)\n2 - полностью изменить данные пользователя\n"))
    return option

def input_newdata():
    new = input("Введите новые данные: ")
    return new

def input_delete():
    d_file = input("Введите пользователя, которого хотите удалить: ")
    return d_file

def input_sort():
    num_sort = int(input("Выберите способ сортировки:\n1 - по ID\n2 - по ФИО\n3 - по номеру\n"))
    return num_sort

# id, ФИО, дата рождения
# 1) Ввод нового пользователя
# 2) Поиск по определённой характеристике
