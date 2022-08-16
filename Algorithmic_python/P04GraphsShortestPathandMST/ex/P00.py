from queue import PriorityQueue

class Edges:
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
    graph[source].append(Edges(source, destination, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys())
distance = [float('inf')] * (max_node + 1)
parent = [0] * (max_node + 1)

distance[start] = 0
pq = PriorityQueue()
pq.put((0, start))

while pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break

    for edge in graph[node]:
        if distance[edge] == float('inf'):
            new_distance = min_distance + edge.weight

            if new_distance < distance[edge.destination]:
                distance[edge.destination] = new_distance
                parent[edge.destination] = node
                pq.put((new_distance, edge.destination))









