# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
number_a = int(input('Введите число: '))
index = 1
fib_1 = 0
fib_2 = 1
while fib_2 <= number_a:
    if fib_2 ==number_a:
        print(index)
        break
    fib = fib_1
    fib_1 = fib_2
    fib_2 += fib
    index += 1
else:
    print(-1)
