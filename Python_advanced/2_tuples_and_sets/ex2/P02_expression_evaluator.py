from collections import deque

operation ={
    '+':lambda x,y: x + y,
    '*':lambda x,y: x * y,
    '-':lambda x,y: x - y,
    '/':lambda x,y: x // y if y != 0 else 'Dived 0',
}

line = input().split()

queue = deque()

for symbols in line:
    if symbols.lstrip('-').isdigit():
        queue.append(int(symbols))
    else:
        while len(queue) > 1:
            a = queue.popleft()
            b = queue.popleft()
            queue.appendleft(operation[symbols](a,b))

print(*queue)



