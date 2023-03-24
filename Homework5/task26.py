# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.
number = int(input('Введите число: '))
number_degree = int(input('Введите степень: '))


def degree(num1: int, num2: int) -> int:
    if num2 == 0:
        return 1
    return num1 * degree(num1, num2-1)


print(degree(number, number_degree))