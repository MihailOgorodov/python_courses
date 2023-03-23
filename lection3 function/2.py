# Функция, когда не известно количество аргументов на вход

def sum_str(*args):  # чтобы передать неограниченное количество аргументов, пишем *
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'n'))
print(sum_str('q', 'e', 'n', 'q', 'b'))
