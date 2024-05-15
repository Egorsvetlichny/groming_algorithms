# Алгоритм сортировки списка по возрастанию методом выбора

def find_index_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    res = []

    for i in range(len(arr)):
        smallest_i = find_index_smallest(arr)
        res.append(arr.pop(smallest_i))

    return res


if __name__ == '__main__':
    my_list = [5, 3, 0, -2, -1, 15, 0, -6, 2, 10]
    print("Исходный массив:", my_list)
    print("Отсортированный по возрастанию массив:", selection_sort(my_list))
