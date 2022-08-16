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
    nodess = queue.popleft()

    if nodess == destination_node:
        break

    for child in graph[nodess]:
        if visited[child]:
            continue
        visited[child] = True
        queue.append(child)
        parent[child] = nodess

path = deque()
nodess = destination_node

while nodess is not None:
    path.appendleft(nodess)
    nodess = parent[nodess]

print(len(path))
print(*path,sep =' ')