# Алгоритм сортировки списка по возрастанию методом пузырька


from typing import Tuple


def buble_sort(arr: list) -> Tuple[list, int]:
    counter = 0  # счётчик сдвигов элементов во время сортировки

    for run in range(len(arr) - 1):
        for i in range(len(arr) - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                counter += 1

    return arr, counter


if __name__ == '__main__':
    my_list = list(map(int, input("Введите элементы массива через пробел: ").split()))

    sorted_list, shift_counter = buble_sort(my_list)
    print("Отсортированный по возрастанию массив: ", sorted_list)
    print("Количество сдвигов элементов во время сортировки: ", shift_counter)
