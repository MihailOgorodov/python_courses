# Дана упорядоченная последовательность an чисел от 1 до N.
# Из копии данной последовательности bn удалили одно число, а оставшиеся перемешали. Найти удаленное число.
import random

n = int(input('Введите длину последовательности: '))

first_list = [i for i in range(1, n + 1)]
set_first_list = set(first_list)
print(f'Последовательность an {first_list}')
first_list.pop(int(input('Введите какой элемент удалить: ')))
random.shuffle(first_list)
print(f'Последовательность bn {first_list}')
set1 = set(first_list)
print(set1)
print(set_first_list.difference(set1))
