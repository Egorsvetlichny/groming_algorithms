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
def alg_Deyk(gr, cos, paren):
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


# Реализация взвешенного графа
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
print(graph)

# Создание таблицы стоимостей
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Создание хеш-таблицы родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

# Массив для отслеживания всех обработанных узлов
processed = []

print()

# Передаём в функцию алгоритма Дейкстры наш подготовленный взвешенный граф,
# таблицу стоимостей и хеш-таблицу родителей.
print("Кратчайшее расстояние из узла 'start' в узел 'fin' равно:", alg_Deyk(graph, costs, parents))
