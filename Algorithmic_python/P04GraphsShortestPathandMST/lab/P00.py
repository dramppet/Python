from collections import deque
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

stat_node = int(input())
destination_node = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[stat_node] = True
queue = deque([stat_node])

while queue:
    node_par = queue.popleft()

    if node_par == destination_node:
        break

    for child in graph[node_par]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = node_par

path = deque()
node_par = destination_node

while node_par is not None:
    path.appendleft(node_par)
    node_par = parent[node_par]

print(len(path))
print(*path,sep =' ')