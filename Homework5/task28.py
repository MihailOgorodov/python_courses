# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
number_1 = int(input('Введите число a: '))
number_2 = int(input('Введите число b: '))


def rec_sum(num_a: int, num_b: int) -> int:
    if num_b == 0:
        return num_a
    return rec_sum(num_a + 1, num_b - 1)


print(f'{number_1} + {number_2} = {rec_sum(number_1, number_2)}')
