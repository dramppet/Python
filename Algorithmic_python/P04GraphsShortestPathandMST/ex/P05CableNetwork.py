from queue import PriorityQueue


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


budget = int(input())
nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes)]

tree = set()
for _ in range(edges):
    edge_data = input().split()
    start, end, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    graph[start].append(Edge(start, end, weight))
    graph[end].append(Edge(start, end, weight))

    if len(edge_data) == 4:
        tree.add(start)
        tree.add(end)

pq = PriorityQueue()

for node in tree:
    for edge in graph[node]:
        pq.put(edge)

budget_used = 0

while not pq.empty():
    min_edge = pq.get()
    not_tree_node = None

    if min_edge.start in tree and min_edge.end not in tree:
        not_tree_node = min_edge.end
    elif min_edge.end in tree and min_edge.start not in tree:
        not_tree_node = min_edge.start

    if not_tree_node is None:
        continue

    if budget_used + min_edge.weight > budget:
        break

    budget_used += min_edge.weight
    tree.add(not_tree_node)
    for edge in graph[not_tree_node]:
        pq.put(edge)

print(f'Budget used: {budget_used}')
