from stack import Stack

vert = (
    (0, 1),
    (1, 2),
    (2, 3),
    (1, 5),
    (1, 4),
    (3, 7),
    (3, 5),
    (5, 7),
    (4, 6),
    (6, 8),
    (5, 8),
    (8, 9),
    (7, 9),
    (1, 10),
    (10, 9),
    (11, 12),
    (11, 13),
    (12, 14),
    (12, 15),
)
vert_2 = (
    (0, 1),
    (0, 4),
    (0, 5),
    (1, 2),
    (1, 6),
    (2, 3),
    (2, 7),
    (3, 4),
    (3, 8),
    (4, 9),
    (5, 7),
    (5, 8),
    (6, 8),
    (6, 9),
    (7, 9),
)

graph_3 = [
    [1, 4, 5],
    [0, 2, 6],
    [1, 3, 7],
    [2, 4, 8],
    [0, 3, 9],
    [0, 7, 8],
    [1, 8, 9],
    [2, 5, 9],
    [3, 5, 6],
    [4, 6, 7],
]


def createGraph(vertexes):
    graph = {}
    for i, j in vertexes:
        if not graph.get(i):
            graph[i] = set()
        if not graph.get(j):
            graph[j] = set()
        graph[i].add(j)
        graph[j].add(i)
    return graph


def createGraphList(vertexes):
    graph = {}
    for i, j in vertexes:
        if not graph.get(i):
            graph[i] = set()
        if not graph.get(j):
            graph[j] = set()
        graph[i].add(j)
        graph[j].add(i)

    linkedList = [None] * len(graph.keys())
    for key in graph:
        val = list(graph[key])
        val.sort()
        linkedList[key] = val

    return linkedList


def dfs(start_vertex, graph):

    used = set()
    distance = {start_vertex: 0}
    parant = {}
    parant[start_vertex] = start_vertex
    _stack = Stack()
    _stack.push(start_vertex)
    while not _stack.isEmpty():
        vertex = _stack.pop()

        for item in graph[vertex]:
            if not distance.get(item) and item != start_vertex:
                distance[item] = distance[vertex] + 1
                parant[item] = vertex
            # if item == end_vertex:
            #     print(used)
            #     return distance[end_vertex]
            if item not in used:
                # print(item)
                used.add(item)
                _stack.push(item)
        used.add(vertex)
    return distance, parant


def dfs_2(v, graph):
    visited = {v}
    to_explore = [v]
    lens = dict()
    lens[v] = 0
    while to_explore:
        u = to_explore.pop()
        print(u)
        new_verteces = [i for i in graph[u] if i not in visited]
        for i in new_verteces:
            lens[i] = lens[u] + 1
        to_explore.extend(new_verteces)
        visited.update(new_verteces)
    return lens


def bfs_2(v, graph):
    visited = {v}
    to_explore = [v]
    lens = dict()
    lens[v] = 0
    while to_explore:
        u = to_explore.pop(0)
        new_verteces = [i for i in graph[u] if i not in visited]
        for i in new_verteces:
            lens[i] = lens[u] + 1

        to_explore.extend(new_verteces)
        visited.update(new_verteces)
    return lens


graph = createGraph(vert)
graph_2 = createGraphList(vert)
# print(dfs(5, 7, graph))
# print(dfs(1, 7, graph))
# print(dfs(1, graph_2))
print(dfs_2(0, graph_3), end="\n\n")
# print(bfs_2(0, graph_3), end='\n\n')

print(dfs(0, graph_3), end="\n\n")
