def main_menu():
    print('Главное меню')
    print('1. Показать весь справочник')
    print('2. Добавить новую запись')
    print('3. Редактировать запись')
    print('4. Поиск контакта')
    print('5. Удалить контакт')
    print('6. Вернуться в главное меню')


def show_directory():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for i in data:
        print(i)


def add_contact():
    file = open('sample.txt', 'a', encoding='UTF-8')
    data = input('Введите фамилию, телефон, комментарий, разделяя все ; ')
    file.write(f'\n{data}')
    file.close()


def edit_contact():
    file = open('sample.txt', 'r', encoding='UTF-8')
    find_element = input('Введите поисковой запрос: ')
    data = file.readlines()
    for item in data:
        if find_element in item:
            print(item)
    file.close()
    file = open('sample.txt', 'a', encoding='UTF-8')
    new_item = input('Для редактирования контакта введите фамилию, телефон, комментарий, разделяя все ; ')
    item = item.replace(item, new_item)
    file.write(f'\n{data}')
    file.close()


def find_contact():
    find_element = input('Введите поисковой запрос: ')
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if find_element in item:
            print(item)
            break
    print('Контакт не найден')
    file.close()

def delete_contact():
    find_element = input('Введите поисковой запрос: ')
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if find_element in item:
            print(item)
            item = item.replace(item,'')


main_menu()
while True:
    choose = int(input('Введите пункт меню: '))
    if choose == 1:
        show_directory()
    if choose == 2:
        add_contact()
    if choose == 3:
        edit_contact()
    if choose == 4:
        find_contact()
    if choose == 5:
        delete_contact()
    if choose == 6:
        main_menu()
