from collections import deque

def dfs(node, graph,visited,component):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited, component)
    component.append(node)
nodes = int(input())

graph = []

for _ in range(nodes):
    line = input()
    children = [] if line == ' ' else [int(x) for x in line.split()]
    graph.append(children)

visited = [None] * nodes
component = deque()
for node in range(len(graph)):
    dfs(node, graph, visited, component)
    print(component)