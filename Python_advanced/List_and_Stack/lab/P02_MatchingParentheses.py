expression =  input()

stack = []

# for el in range(len(expression)):
#     if expression[el] == '(':
#         stack.append(el)
#     elif expression[el] == ')':
#         start = stack.pop()
#         end = el
#         print(expression[start:end + 1])

for idx, ch in enumerate(expression):
    if ch == '(':
        stack.append(idx)
    elif ch == ')':
        start = stack.pop()
        finish = idx
        print(expression[start:finish + 1])