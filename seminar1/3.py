# Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

train_car_number = int(input('Введите номер вагона, в который сел Витя: '))
train_car_count = int(input('Введите написанный номер вагона: '))
if train_car_count != train_car_number:
    print(f'Количество вагонов {train_car_number + train_car_count - 1}')
else:
    print('Требуются дополнительные условия')
