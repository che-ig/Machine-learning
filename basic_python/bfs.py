from collections import deque

vert = ((1, 2), (2, 3), (1, 5), (1, 4), (3, 7), (3, 5),
         (5, 7), (4, 6), (6, 8), (5, 8), (8, 9), (7, 9))

n = 9 # quantity vertexes in graph

graph = {i:set() for i in range(1, n + 1)}
for i, j in vert:
    graph[i].add(j)
    graph[j].add(i)

def bfs(start_vertex, end_vertex, graph):
    if not graph.get(start_vertex) or not graph.get(end_vertex):
        print('Error')
        return
    distance = {
        start_vertex: 0
    }
    queue = deque([start_vertex])
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not distance.get(neighbor):
                distance[neighbor] = distance[v] + 1
                if neighbor == end_vertex:
                    return distance[end_vertex]
                queue.append(neighbor)
    return distance

print(bfs(5, 7, graph))
print(bfs(1, 7, graph))
print(bfs(2, 9, graph))
print(bfs(9, 1, graph))
