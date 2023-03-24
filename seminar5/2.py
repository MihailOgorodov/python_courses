# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
import math


def num_check(num: int) -> bool:
    if num in [1, 2, 3]:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        return True


print(num_check(3))
