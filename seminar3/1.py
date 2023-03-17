# Дан список чисел. Определите, сколько в нем встречается различных чисел.
import random
num_list = [random.randint(0,20) for _ in range(30)]

print(num_list)

num_set = set(num_list)

print(num_set)
print(len(num_set))