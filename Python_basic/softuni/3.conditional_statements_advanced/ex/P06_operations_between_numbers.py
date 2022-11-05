num1 = int(input())
num2 =int(input())
sign = input()


if sign == '+':
    operation = num1 + num2
    if operation % 2 == 0:
        print(f'{num1} {sign} {num2} = {operation} - even')
    else:
        print(f'{num1} {sign} {num2} = {operation} - odd')
elif sign == '-':
    operation = num1 - num2
    if operation % 2 == 0:
        print(f'{num1} {sign} {num2} = {operation} - even')
    else:
        print(f'{num1} {sign} {num2} = {operation} - odd')
elif sign == '*':
    operation = num1 * num2
    if operation % 2 == 0:
        print(f'{num1} {sign} {num2} = {operation} - even')
    else:
        print(f'{num1} {sign} {num2} = {operation} - odd')
elif sign == '/':
    if num1 == 0:
        print(f'Cannot divide {num1} by zero')
    elif num2 == 0:
        print(f'Cannot divide {num2} by zero')
    else:
        operation = num1 / num2
        print(f'{num1} {sign} {num2} = {operation:.2f}')
elif sign == '%':
    if num1 == 0:
        print(f'Cannot divide {num1} by zero')
    elif num2 == 0:
        print(f'Cannot divide {num2} by zero')
    else:
        operation = num1 % num2
        print(f'{num1} {sign} {num2} = {operation}')
