# Алгоритм сортировки списка по возрастанию методом слияния

# Функция, объединяющая два списка
def merge_two_lists(a, b):
    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]

    return c


# Функция, выполняющая сортировку
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        return merge_two_lists(left, right)


if __name__ == '__main__':
    my_list = [23, 0, 12, -3, 2, 3, 10, 1, -1, 0, 4]
    print("Исходный массив:", my_list)
    print("Отсортированный по возрастанию массив: ", merge_sort(my_list))
