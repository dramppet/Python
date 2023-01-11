from collections import deque

queue = deque([int(x) for x in input().split()])
capacity_rack = int(input())

count_rack = 0
rack = 1

while queue:
    element = queue[0]
    if rack + element < capacity_rack:
        rack += element
        queue.popleft()
    else:
        count_rack += 1
        rack = 0
print(queue)
print(count_rack)
