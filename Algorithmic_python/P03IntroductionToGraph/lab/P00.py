from collections import deque
def dfs(node, graph, visite):
    result = deque()
    if node in visite:
        return

    visite.add(node)

    for child in graph[node]:
        dfs(child, graph, visite)
    result.append(node)



nodes = int(input())

graph = {}

for node in range(nodes):
    line_str = input()

    if len(line_str) > 0:
        graph[node] = [int(x) for x in line_str.split()]
    else:
        graph[node] = []

visited = set()

for node in graph:
    dfs(node, graph, visited)