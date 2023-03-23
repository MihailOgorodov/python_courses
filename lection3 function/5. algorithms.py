# быстрая сортировка
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой
# должен отгадать. Согласитесь, что мы можем перебирать эти значения в случайном
# порядке, например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, но что
# если мы обратиться к стратегии “разделяй и властвуй” Обозначим друзей, друг_1
# это Иван, который загадал число, друг_2 это Петр, который отгадывает

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([14, 5, 9, 10, 11, 12, 11]))


# сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        rigth = nums[mid:]
        merge_sort(left)
        merge_sort(rigth)
        i = j = k = 0
        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = rigth[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(rigth):
            nums[k] = rigth[j]
            j += 1
            k += 1

list_11 = [1,2,3,4,5,63,231,1,234,456,756,2,345]
merge_sort(list_11)
print(list_11)
