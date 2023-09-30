# нахождение суммы элементов массива через цикл
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

# нахождение суммы элементов массива через рекурсивную функцию
def recursion_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + recursion_sum(arr)


print(sum([1, 2, 3, 4, 5]))
print(recursion_sum([1, 2, 3, 4, 5]))
