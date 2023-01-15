from collections import deque

potatoes = input().split(' ')
potatoes_queue = deque(potatoes)
step = int(input())

while potatoes_queue:
    for _ in range(step - 1):
        potatoes_queue.append(potatoes_queue.popleft())
    potato_to_remove = potatoes_queue.popleft()
    if potatoes_queue:
        print(f'Removed {potato_to_remove} ')
    else:
        print(f'Last is {potato_to_remove} ')