# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

count_first_class = int(input('Введите количество учеников в первом классе: '))
count_second_class = int(input('Введите количество учеников во втором классе: '))
count_third_class = int(input('Введите количество учеников в третьем классе: '))

print(f'Количество парт для учащихся {(count_first_class+count_second_class+count_third_class+1)//2}')