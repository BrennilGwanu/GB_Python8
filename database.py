def write_name(inf):
    with open ("phonebook.txt","a",encoding = "UTF-8") as file:
        file.writelines(inf)

def read_found(search):
    with open ("phonebook.txt","r",encoding = "UTF-8") as file:
        list = file.readlines()
        for word in list:
            if search in word:
                print(word)

def change_part(var, new):
    with open ("phonebook.txt","r",encoding = "UTF-8") as file:
        list = file.read()
        list = list.replace(var, new)
    with open ("phonebook.txt","w",encoding = "UTF-8") as file:
        file.write(list)
    

def delete(num):
     with open ("phonebook.txt","r+",encoding = "UTF-8") as file:
        list = file.readlines()
        file.seek(0)
        for i in list:
            if num not in i.strip("\n"):
                file.write(i)
            file.truncate()

def sort(type):
    with open ("phonebook.txt","r",encoding = "UTF-8") as file:
        mas = file.readlines()
        if type == 1 or type == 3:
            mas.sort(key = lambda x: int(x.split(",") [type - 1]))
        else:
            mas.sort(key = lambda x: x.split(",") [type - 1])
        for user in mas:
            print(user)

def all_users():
    with open ("phonebook.txt","r",encoding = "UTF-8") as file:
        print(file.read())