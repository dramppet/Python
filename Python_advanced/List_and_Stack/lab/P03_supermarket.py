from collections import deque
queue = deque()

COMMAND_PAID = 'Paid'
COMMAND_END = "End"

while True:
    name = input()
    if name == COMMAND_END:
        print(f"{len(queue)} people remaining.")
        break
    elif name == COMMAND_PAID:
        while queue:
            print(queue.popleft())

    else:
        queue.append(name)