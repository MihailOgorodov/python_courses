# print(5)
# n = 5
# print(n)
# n = str
# print(type(n)) - вывод типа данных
# b = 1
# c = 1.58
# a = 'trap'
# Интерполяция
# print(f"{a} -= {b}=-0 {c}")
# print("{} = {} - {}" .format(a, b, c))
# print('Введите число a')
# a = int(input())
# b = int(input('Введите число b '))

# print(a, '+', b, '=', a + b)
# print(f"Квадрат числа {a} = {a*a}")

# a = 'qwerty'
# # print(a[0])
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

text='Съешь еще булок'
#print(len(text)) # длина строки
#print('еще' in text) # проверка есть ли строка в строке
#print(text.lower()) # перевод в нижний рестр
#print(text.upper()) # перевод в верхний рестр
#print(text.replace('еще','ЕЩЕ')) # замена исходного текста на текст
#отрицательная индексация
print(text[-1]) # последний элемент строки
print(text[:]) # вся строка
print(text[:2])# первые 2 элемента
print(text[len(text)-2])
print(text[len(text)-2:]) # вывод от 2 с конца элемента до последнего
print(text[2:9]) #от 2 до 9
print(text[0:-2])#от 1 до 2 с конца
print(text[0:len(text):2]) # от 0 элемента, до конца длины строки, с шагом 2
print(text[::2])# от начало до конца с шагом 2
text = text[2:9] + text[-5] + text[len(text)-2]
print(text)