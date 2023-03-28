# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
import random

lists_size = tuple(map(int, input('Введите размеры списков через пробел: ').split()))

list_1 = set([random.randint(0, 10) for _ in range(lists_size[0])])
print(list_1)
list_2 = set([random.randint(0, 10) for _ in range(lists_size[1])])
print(list_2)
result_list = list_1.difference(list_2)
print(result_list)
print('')
list_3 = [random.randint(0, 10) for _ in range(lists_size[0])]
print(list_3)
list_4 = [random.randint(0, 10) for _ in range(lists_size[1])]
print(list_4)
result_list_2 = [item for item in list_3 if item not in list_4]
print(result_list_2)


