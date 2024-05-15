# Алгоритм сортировки списка по возрастанию методом вставок


from typing import Tuple


def insertion_sort(arr: list) -> Tuple[list, int]:
    counter = 0  # счётчик сдвигов элементов во время сортировки

    for run in range(1, len(arr)):
        for i in range(run, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                counter += 1
            else:
                break

    return arr, counter


if __name__ == '__main__':
    my_list = list(map(int, input("Введите элементы массива: ").split()))

    sorted_list, shift_counter = insertion_sort(my_list)
    print("Отсортированный по возрастанию массив: ", sorted_list)
    print("Количество сдвигов элементов во время сортировки: ", shift_counter)
