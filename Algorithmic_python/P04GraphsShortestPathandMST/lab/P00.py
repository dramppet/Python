from collections import deque
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destinacion = [int(x) for x in input().split()]
    graph[source].append(destinacion)

starrt_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[starrt_node] = True
queue = deque([starrt_node])

while queue:
    node = queue.popleft()

    if node == destination_node:
        break

    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node

path = deque()
node = destination_node

while node is not None:
    path.appendleft(node)
    node = parent[node]
print(len(path) - 1)
print(*path, sep = ' ')

