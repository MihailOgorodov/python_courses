# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
# import random
#
# k = 10  # количество 4значных чисел
# num_array = []
#
# for _ in range(0, k + 1):
#     num_array.append(random.randint(1000, 10000))
# print('1 этап: ', num_array)
#
# # 2
# num = int(input('Введите цифру: '))
# for i in range(0, len(num_array)):
#     temp = num_array[i]
#     temp2 = 0
#     while temp > 0:
#         if temp % 10 == num:
#             pass
#         else:
#             temp2 = temp2 * 10 + temp % 10
#         temp //= 10
#     num_array[i] = temp2
# print(num_array)
#
# # 3
# for i in range(0, len(num_array)):
#     while num_array[i] > 9:
#         num_array[i] = int(num_array[i] / 100) + (num_array[i] % 100 - num_array[i] % 10) // 10 + num_array[i] % 10
# print('сумма цифр = ', num_array)
#
# #4
# num_array = set(num_array)
# print(num_array)
import random

my_list = [random.randint(1000, 9999) for _ in range(10)]
print(my_list)

number = input('Введите число: ')
for i in range(len(my_list)):
    my_list[i] = str(my_list[i]).replace(number, '')
print(my_list)

for i in range(len(my_list)):
    while len(my_list[i]) > 1:
        summa = 0
        # my_list[i] = str(sum(list(map(int, list(my_list[i])))))  # функция map применяет int ко всем элементам листа my_list
        for elem in my_list[i]:
            summa += int(elem)
        my_list[i] = str(summa)
print(my_list)

print(set(my_list))
