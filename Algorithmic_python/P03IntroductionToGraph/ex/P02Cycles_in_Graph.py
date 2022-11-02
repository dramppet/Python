def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}

while True:
    line = input()

    if line == 'End':
        break

    sorce, destination = line.split('-')
    if sorce not in graph:
        graph[sorce] = []
    if destination not in graph:
        graph[destination] = []

    graph[sorce].append(destination)

visited = set()
try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
