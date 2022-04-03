n1 = int(input())
n2 = int(input())
operator = input()

result = 0
different = ''

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        different = 'even'
    else:
        different = 'odd'
elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        different = 'even'
    else:
        different = 'odd'
elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        different = 'even'
    else:
        different = 'odd'
elif operator == '/':
    if n1 == 0:
        print(f'Cannot divide {n2} by zero')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1/ n2
        print(f'{n1} / {n2} = {result}')
elif operator == '%':
    if n1 == 0:
        print(f'Cannot divide {n2} by zero')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1% n2
        print(f'{n1} % {n2} = {result}')


if operator == '+' or operator == '-' or operator == '*':
    print(f'{n1} {operator} {n2} = {result} - {different}')
