# алгоритм быстрой сортировки массива по возрастанию с помощью рекурсии

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [item for item in arr[1:] if item < pivot]
        greater = [item for item in arr[1:] if item > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([]))
    print(quick_sort([17]))
    print(quick_sort([10, 5, 2, 3]))
    print(quick_sort([4, 2, 7, 23, 13, 1, 8, 0]))

    assert quick_sort([4, 2, 7, 23, 13, 1, 8, 0]) == [0, 1, 2, 4, 7, 8, 13, 23]
