from collections import deque
working_bee = deque(int(x) for x in input().split())
line_nectar = deque(int(x) for x in input().split())
line_symbols = deque(input().split())

honey = 0

operation = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a / b if b  > 0 else None,
}

while working_bee and line_nectar:


    bee = working_bee.popleft()
    nectar = line_nectar.pop()

    if nectar < bee:
        working_bee.appendleft(bee)
    elif nectar > bee:
        honey += abs(operation[line_symbols.popleft()](bee,nectar))

print(f"Total honey made: {honey}")

if working_bee:
    print(f"Bees left: {', '.join(str(x) for x in working_bee)}")
if line_nectar:
    print(f"Nectar left: {', '.join(str(x) for x in line_nectar)}")