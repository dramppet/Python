word = input()

stack = []

for w in word:
    stack.append(w)

while stack:
    print(stack.pop(),end='')