import re

def menu():
    while True:
        print("\n1. Показать все контакты\n"
              "2. Добавить контакт\n"
              "3. Изменить контакт\n"
              "4. Найти контакт\n"
              "5. Удалить контакт\n"
              "6. Выход\n")
        number = input("Выберите действие: ")
        if re.search(r'[\D]', number):
            break
        elif int(number) == 6:
            break
        else: 
            numbers_functions(int(number))

def show():
    read()
    print("\n")
    for line in phonebook:
        print(line)

def add():
    name = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    comment = input("Напишите комментарий: ")
    phonebook.append(f'{name}; {phone}; {comment}')
    wright()

def wright():
    result = "\n".join(phonebook)
    with open('phone_book.txt', "w", encoding="utf-8") as f:
        f.write(result)

def read():
    global phonebook
    with open('phone_book.txt', "r", encoding="utf-8") as f:
        read_data = f.read()
        phonebook = read_data.split("\n")

def find():
    print("\n")
    search_string = input("Введите строку поиска: ")
    print("\n")
    for line in phonebook:
        if search_string.lower() in line.lower():
            print(line)

def edit():
    print("\n")
    search_string = input("Введите строку поиска: ")
    find_index = []
    index = 0
    print("\n")
    for line in phonebook:
        if search_string.lower() in line.lower():
            print(line)
            find_index.append(index)
        index += 1
    if len(find_index) > 0 and input("Изменить строки (да/нет)? ") == "да":
        print("\n")
        name = input("Введите ФИО: ")
        phone = input("Введите номер телефона: ")
        comment = input("Напишите комментарий: ")
        for i in find_index:
            lst = phonebook[i].split("; ")
            phonebook[i] = (name if name != '' else lst[0]) + "; " + (phone if phone != '' else lst[1]) + "; " + (comment if comment != '' else lst[2])
        wright()

def delete():
    print("\n")
    search_string = input("Введите строку поиска: ")
    find_lines = []
    index = 0
    print("\n")
    for line in phonebook:
        if search_string.lower() in line.lower():
            print(line)
            find_lines.append(phonebook[index])
        index += 1
    print("\n")
    if len(find_lines) > 0 and input("Удалить строки (да/нет)? ") == "да":
        for line in find_lines:
            phonebook.remove(line)
        wright()

def numbers_functions(argument):
    switcher = {
        1: show,
        2: add,
        3: edit,
        4: find,
        5: delete
    }
    func = switcher.get(argument, lambda: "Invalid value")
    func()
        
phonebook = []
read()
menu()
