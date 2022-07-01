words = input()

reversed_stack = []

for word in words:
    reversed_stack.append(word)

while reversed_stack:
    print(reversed_stack.pop(),end='')
