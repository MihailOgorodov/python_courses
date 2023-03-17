# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
from random import randint

num_list = [_ for _ in range(10)]
shift = 3
print(num_list)
for _ in range(shift):
    num_list.insert(0, num_list.pop())
print(num_list)

second_list = [_ for _ in range(10)]
print(second_list[-shift:] + second_list[:-shift])

