infinity = float('inf')
processd = []
graph = {
    0: {
        1: 5,
        2: 2
    },
    1: {
        3: 4,
        4: 2
    },
    2: {
        1: 8,
        4: 7
    },
    3: {
        4: 6,
        5: 3
    },
    4: {
        5: 1
    },
    5: {}
}
costs = {
    0: 0,
    1: 5,
    2: 2,
    3: infinity,
    4: infinity,
    5: infinity
}
parent = {
    0: None,
    1: 0,
    2: 0
}

def get_least_cost_node(costs):
    ''' 
        Возвращает узел с минимальной стоимостью из тех ухлов,
        которые еще не были в обработке.
    '''
    min_cost = float('inf')
    cost_node = None
    for node in costs:
        cost = costs[node]
        # Ищем узел с минимальной стоимостью из тех котоые еще не обработаны
        if cost < min_cost and node not in processd:
            cost_node = node
            min_cost = cost_node
    return cost_node
        
def deyrstra(graph, costs):
    '''
        Алгоритм Дейкстры вычисляет кратчайший путь во взвешанном графе.
        Важно. Дейкстра работает ТОЛЬКО С положительными весами.
    '''
    # Обновляем словарь стоимостей для каждого узла, если новое значене
    # меньше текущего, тем самым мы находим минимальную стоимость для 
    # каждого узла.
    node = get_least_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parent[n] = node
        processd.append(node)
        node = get_least_cost_node(costs)

def get_near_path(end, parent):
    node = parent[end]
    path = [end]
    max_len_path = len(parent)
    while node is not None and max_len_path:
        path.append(node)
        node = parent[node]
        max_len_path -= 1
    return path[: : -1]

if __name__ == '__main__':
    deyrstra(graph, costs)
    print(costs)
    print(get_near_path(5, parent))
