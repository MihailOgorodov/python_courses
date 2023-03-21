# Словари. Что такое и как использовать
import random

my_dict = {1: 'one', 2: 'two', 3: 'three'}

print(my_dict[1])  # выдача значения словаря. Но лучше так не делать, а делать так

print(my_dict.get(4))  # в этом случае, если такого ключа нет, возвращает NONE и прога не выдает ошибку и не завершается
print(my_dict.get(4, 'Нет такого ключа'))  # в случае NONE выдает заданное значение

# Добавляем новое значение в словарь, но этот способ перезапишет текущий ключ, если он уже есть в словаре
my_dict[4] = 'four'
print(my_dict.get(4, 'Нет такого ключа'))
print(my_dict)

# А этот способ проверит наличие такого же ключа, если он есть, ничего, если нет - добавит новое значение
my_dict.setdefault(5, 'ПЯТЬ')
my_dict.setdefault(3, 'ПЯТЬ')
print(my_dict)

# Задача. Есть список. Нужно подсчитать сколько каждая цифра входит в список

my_list = [random.randint(0, 20) for _ in range(10)]
print(my_list)

count_dict = {}

for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1
print(count_dict)

