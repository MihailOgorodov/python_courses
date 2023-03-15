#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
from random import randint

count_coins = int(input('Введите количество монет на столе: '))
count_heads = 0
count_tails = 0
for i in range(count_coins):
    coins_value = randint(0, 1)
    print(coins_value, end=" ")
    if coins_value < 1:
        count_heads += 1
    else:
        count_tails += 1
if count_heads > count_tails:
    print(f'\nКоличество монет, которое нужно перевернуть = {count_tails}')
else:
    print(f'\nКоличество монет, которое нужно перевернуть = {count_heads}')



