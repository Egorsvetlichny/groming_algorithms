# Реализация алгоритма бинарного поиска
def binary_searh(list, item):
    # задание границ для поиска
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


mylist = [1, 3, 5, 7, 9]  # отсортированный по возрастанию список

print(binary_searh(mylist, 3))
print(binary_searh(mylist, -1))
