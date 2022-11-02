exp = input()

stack = []

for idx in range(len(exp)):
    if exp[idx] == '(':
        stack.append(idx)
    elif exp[idx] == ')':
        start_idx = stack.pop()
        print(exp[start_idx: idx + 1])