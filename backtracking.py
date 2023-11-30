# Решение задачи о рюкзаке. Динамическое программирование. Рекурсивный поиск с возвратом
def backpack_task(available_items, weight):
    result_items = []
    total_price = 0

    def backtrack(items, current_weight, current_price, selected_items):
        nonlocal result_items
        nonlocal total_price

        if not items or current_weight > weight:
            if current_price > total_price:
                total_price = current_price
                result_items = selected_items[:]
            return

        item_name, item_property = items.popitem()
        if item_property['weight'] <= weight - current_weight:
            selected_items.append(item_name)
            backtrack(dict(items), current_weight + item_property['weight'], current_price + item_property['price'],
                      selected_items)
            selected_items.pop()
        backtrack(dict(items), current_weight, current_price, selected_items)

    backtrack(available_items, 0, 0, [])
    return result_items, total_price


def main():
    available_items = {
        'radio': {'price': 4000, 'weight': 4},
        'laptop': {'price': 2000, 'weight': 2},
        'guitar': {'price': 1500, 'weight': 1},
        'knife': {'price': 1700, 'weight': 1},
        'bicycle': {'price': 3000, 'weight': 3},
    }
    weight_of_backpack = 4

    items_taken, total_price = backpack_task(available_items, weight_of_backpack)
    print(f'Для максимальной выгоды были взяты следующие предметы: {items_taken}')
    print(f'Общая выгода всех предметов составила: {total_price}')


if __name__ == '__main__':
    main()
