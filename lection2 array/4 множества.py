# Множества
# 💡 Множества содержат в себе уникальные элементы, не обязательно
# упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два
# множества, Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность. Давайте разберем их.
colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray') # добавляет что-то в множество
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red') # удаляет из множества
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red')  # KeyError: 'red' # нельзя удалить одно и тоже 2 раза
colors.discard('red')  # ok # для этого есть ремове - проверяет, если есть элемент - удаляет, если нет, пропускает
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { } Это пустое множество
print(colors)  # set()

# Операции со множествами в Python
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

#List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна
# из культовых фишек Python — list comprehension (редко переводится на русский, но
# можно использовать определение «генератора списка»). Comprehension легко
# читать, и их используют как начинающие, так и опытные разработчики.
# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке.
# 1. Простая ситуация — список:
list_1 = [exp for item in iterable]
# 2. Выборка по заданному условию:
list_1 = [exp for item in iterable (if conditional)]
# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# 11
# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

