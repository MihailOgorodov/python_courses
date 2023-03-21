# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
import random
import string

my_string = ''.join([random.choice(string.ascii_letters) for _ in range(30)])  # рандомные буквы
print(my_string)

dict_count = {}
for char in my_string:
    dict_count[char] = dict_count.get(char, 0) + 1
    if dict_count.get(char) > 1:
        print(f'{char}_{dict_count.get(char)}', end='')
    else:
        print(char, end='')


# string = input('Введите символы: ')

# first_list = list(string)
# # print(*first_list)
#
# my_dict = dict()
# for item in set(first_list):
#     my_dict.setdefault(item, 0)
# # print(my_dict)
#
# for key, value in my_dict.items():
#     for i in range(len(first_list)):
#         if first_list[i] == key:
#             if value > 0:
#                 first_list[i] = f'{key}_{value}'
#             value += 1
#
# result_str = ''
# for i in first_list:
#     result_str += f'{i} '
# print(result_str)
