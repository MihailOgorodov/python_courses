# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные
# спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из
# пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, # а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна

import random

elips_of_orbits = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(10)]
print(elips_of_orbits)


def find_farthest_orbit(list_of_orbits):
    new_list = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    mult_list = list(map(lambda x: x[0] * x[1] * 3.14, new_list))
    print(max(mult_list))
    print(mult_list.index(max(mult_list)))
    return new_list[mult_list.index(max(mult_list))]


print(find_farthest_orbit(elips_of_orbits))
