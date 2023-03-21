# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.
import string

# in_string = input('Введите текст: ').lower()
#
# strings = in_string.split()
# # print(strings)
#
# set_1 = set()
# for i in range(0, len(strings)):
#     if strings[i] not in set_1:
#         set_1.add(strings[i])
#
# print(set_1)
# print('Уникальных слов введено: ', len(set_1))

my_string = input('Введите текст: ')
for char in string.punctuation:
    my_string = my_string.replace(char, ' ')  # замена всех знаков препинания пробелами
my_string = my_string.lower().split()
print(len(set(my_string)))