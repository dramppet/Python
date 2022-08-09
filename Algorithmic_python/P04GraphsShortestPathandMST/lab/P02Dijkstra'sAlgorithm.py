class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(Edge(source, destination, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys())

distance = [0] * (max_node + 1)
parent = [None] * (max_node + 1)
