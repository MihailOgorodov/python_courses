# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random

count_one = int(input('Введите кол-во элементов первого множества: '))
count_two = int(input('Введите кол-во элементов второго множества: '))

my_list_one = [random.randint(0, 100) for _ in range(count_one)]
print(my_list_one)

my_list_two = [random.randint(0, 100) for _ in range(count_two)]
print(my_list_two)

my_list_result = set(my_list_one).union(set(my_list_two))

my_list_result = list(my_list_result)

for i in range(len(my_list_result)):
    for j in range(i + 1, len(my_list_result)):
        if my_list_result[i] > my_list_result[j]:
            my_list_result[i], my_list_result[j] = my_list_result[j], my_list_result[i]

print(my_list_result)
