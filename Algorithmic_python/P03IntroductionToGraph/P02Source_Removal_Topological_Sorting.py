def find_depencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1

    return result


def fine_node_witfout_dependencies(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node

    return None

nodes = int(input())

graph = {}

for _ in range(nodes):
    lin_parts = input().split('->')
    node = lin_parts[0].strip()
    children = lin_parts[1].strip().split(', ') if lin_parts[1] else []
    graph[node] = children

dependencies_by_node = find_depencies(graph)

has_cycle = False
sorted_nodes = []
while dependencies_by_node:
    node_to_remove = fine_node_witfout_dependencies(dependencies_by_node)

    if node_to_remove is None:
        has_cycle = True
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycle:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

