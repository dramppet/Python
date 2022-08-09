nodes = int(input())
pairs  = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(nodes):
   node, children_str =  input().split(':')
   children =[int(x) for x in children_str.split(' ') ]if children_str else []
