graph = {
    1 : [2, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: [],
}
visitd = set()

def dfs

for node in graph:
    dfs(node, graph, visitd)