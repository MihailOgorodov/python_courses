# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
import random

num_list = [random.randint(0, 20) for _ in range(10)]
print(num_list)
sum = 0
for i in range(1, len(num_list)):
    if num_list[i-1] < num_list[i]:
        sum += 1
print(sum)

# или так
new_list = [i for i in range(1, len(num_list)) if num_list[i] > num_list[i-1]]
print(len(new_list))
