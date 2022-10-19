exp = input()

stack = []

for idx, ch in enumerate(exp):
    if ch == '(':
        stack.append(idx)
    elif ch == ')':
        clos_idx = idx
        open_idx = stack.pop()
        print(exp[open_idx: clos_idx + 1])