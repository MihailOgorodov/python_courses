# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

origami_count = int(input('Введите количество журавликов, которое сделали дети: '))

katya_origami_count = (origami_count // 6) * 4
petya_origami_count = origami_count // 6
print(f'Петя сделал {petya_origami_count}\n'
      f'Катя сделала {katya_origami_count} \n'
      f'Сережа сделал {petya_origami_count} ')
