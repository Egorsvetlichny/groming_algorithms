# нахождение количества элементов массива через цикл
def count(arr):
    i = 0
    for i in range(len(arr)):
        i += 1
    return i


# нахождение количества элементов массива через рекурсивную функцию
def recursion_count(arr):
    if arr == []:
        return 0
    else:
        del arr[0]
        return 1 + recursion_count(arr)


print(count([1, 2, 3, 4, 5]))
print(recursion_count([1, 2, 3, 4, 5]))