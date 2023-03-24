# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.

def degree(num1: int, num2: int) -> int:
    if num2 == 0:
        return 1
    return num1 * degree(num1, num2-1)

print(degree(3,3))