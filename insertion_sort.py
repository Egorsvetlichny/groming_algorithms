# Алгоритм сортировки списка по возрастанию методом вставок

len_arr = int(input("Введите длину массива: "))
arr = list(map(int, input("Введите элементы массива: ").split()))
count = 0  # счётчик сдвигов элементов во время сортировки

for run in range(1, len_arr):
    for i in range(run, 0, -1):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            count += 1
        else:
            break

print("Отсортированный по возрастанию массив: ", *arr)
print("Колисество сдвигов элементов во время сортировки: ", count)