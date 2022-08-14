nodes = int(input())

graph = []

for node in range(nodes):
    line_str = input()

    if len(line_str) > 0:
        graph.append([int(x) for x in line_str.split()])
    else:
        graph.append([])

visited = set()

