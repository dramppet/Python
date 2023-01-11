line_row = int(input())
stack = []

for _ in range(line_row):
    line = input().split()
    command = int(line[0])

    if command == 1:
        stack.append(line[1])
    elif command == 2:
        if len(stack) > 0:
            stack.pop()
    elif command == 3:
        print(max(stack))
    elif command == 4:
        print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(),end=', ')
    else:
        print(stack.pop())