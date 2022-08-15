nodes = int(input())

graph = []

for _ in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(children):
        if state in 'Y':
            children.append(idx)
    graph.append(children)
