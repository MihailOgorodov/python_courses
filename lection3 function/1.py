# Функции
def sum_numbers(n):  # так обозначается функция def, потом имя, и переменная
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sum_numbers(5)


def sum_numbers2(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


print(sum_numbers2(7))


def sum_numbers3(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa  # return завершает работу функции. Все, что ниже - не будет работать


a = sum_numbers3(5)
print(a)


def sum_numbers4(n, y='Hello'):  # значение аргумента по умолчанию
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


a = sum_numbers4(6, 'qwerrty')      # если аргумент передаем, то он заменит значение по умолчанию
print(a)
