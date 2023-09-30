# Алгоритм сортировки списка по возрастанию методом пузырька

len_arr = int(input("Введите длину массива: "))
arr = list(map(int, input("Введите элементы массива: ").split()))
count = 0  # счётчик сдвигов элементов во время сортировки

for run in range(len_arr - 1):
    for i in range(len_arr - 1 - run):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] =  arr[i + 1], arr[i]
            count += 1

print("Отсортированный по возрастанию массив: ", *arr)
print("Колисество сдвигов элементов во время сортировки: ", count)