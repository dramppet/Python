words = input()

stack = []

for ch in words:
    stack.append(ch)

while stack:
    print(stack.pop(),end='')
