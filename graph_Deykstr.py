# Нахождение узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


# Реализация алгоритма Дейкстры
def dijkstra_algorithm(gr, cos, paren):
    node = find_lowest_cost_node(cos)

    while node is not None:
        cost = cos[node]
        neighbors = gr[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if cos[n] > new_cost:
                cos[n] = new_cost
                paren[n] = node

        processed.append(node)
        node = find_lowest_cost_node(cos)

    return cos["fin"]


if __name__ == '__main__':
    # Реализация взвешенного графа
    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }

    # Создание таблицы стоимостей
    infinity = float("inf")
    start_costs = {"a": 6, "b": 2, "fin": infinity}

    # Создание хеш-таблицы родителей
    parents = {"a": "start", "b": "start", "fin": None}

    # Массив для отслеживания всех обработанных узлов
    processed = []

    print(graph)

    # Передаём в функцию алгоритма Дейкстры наш подготовленный взвешенный граф,
    # таблицу стоимостей и хеш-таблицу родителей.
    print("Кратчайшее расстояние из узла 'start' в узел 'fin' равно:", dijkstra_algorithm(graph, start_costs, parents))
