from collections import deque

food = int(input())
queue = deque([int(x) for x in input().split()])
print(max(queue))

while queue:
    element = queue[0]
    if food >= element:
        food -= queue[0]
        queue.popleft()
    else:
        break

if queue:
    print("Orders left:", end=' ')
    while queue:
        print(queue.popleft(),end = ' ')

else:
    print('Orders complete')