from database import *
from view import *

def main():
    while True:
        num = input_num()
        if num == 1:
            name = input_name()
            write_name(name)
            print("Успешно записано")
        if num == 2:
            search_data = input_found()
            read_found(search_data)
            print("Успешно найдено")
        if num == 3:
            char = input_change()
            sel = input_choice()
            if sel == 1:
                new_data = input_newdata()
                change_part(char, new_data)
            else:
                delete(char)
                write_name(input_name())
            print("Изменения внесены")
        if num == 4:
            d = input_delete()
            delete(d)
            print("Удалено")
        if num == 5:
            t = input_sort()
            sort(t)
        if num == 6:
            all_users()
        if num == 7:
            break

main()