# нахождение максимального числа в массиве с помощью цикла
def max_in_arr(arr):
    if len(arr) != 0:
        max = arr[0]
    else:
        return 'Array is empty!'

    for el in arr:
        if el > max:
            max = el
    return max


# нахождение максимального числа в массиве с помощью рекурсии
def recursion_maxInArr(arr):
    if len(arr) == 0:
        return 'Array is empty!'
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = recursion_maxInArr(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max_in_arr([1, 3, 4, 5, 2]))
print(recursion_maxInArr([1, 3, 4, 5, 2]))

