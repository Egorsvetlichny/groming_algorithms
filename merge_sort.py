# Алгоритм сортировки списка по возрастанию методом слияния

# Фукция, объединяющая два списка
def merge_two_list(a, b):
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


# Функция, выполняющаяя сортировку
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge_two_list(left, right)


len_arr1 = int(input("Введите длину массива: "))
arr1 = list(map(int, input("Введите элементы массива: ").split()))
print("Отсортированный по возрастанию массив: ", *merge_sort(arr1))