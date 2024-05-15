# Реализация алгоритма бинарного поиска


def binary_search(arr, item):
    # задание границ для поиска
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]  # отсортированный по возрастанию список
    print("Исходный список: ", my_list)

    print()

    print("Номер элемента 3 в списке:", binary_search(my_list, 3))
    print("Номер элемента 9 в списке:", binary_search(my_list, 9))
    print("Номер элемента -1 в списке:", binary_search(my_list, -1))
