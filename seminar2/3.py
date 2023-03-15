# Про оттепель. Найти количество подряд теплых дней (больше 0). Их интересует, сколько дней длилась самая
# длинная оттепель. Вводится N = количество дней всего
from random import randint

day = int(input("Введите количество дней - "))

count = 0
count_day = 0
warm_days = 0
temp = randint(-3, 3)
while count <= day:
    temp = temp + randint(-3, 3)
    if temp > 0:
        count_day += 1
    else:
        if warm_days < count_day:
            warm_days = count_day
        count_day = 0
    count += 1
    print(temp, end=' ')
else:
    if warm_days < count_day:
        warm_days = count_day
    # print(warm_days, end=' ')
print()
print(warm_days)
