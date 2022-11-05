num1 = int(input())
num2 =int(input())
sign = input()

result = None


if sign == '+':
    result = f'{num1} + {num2} = {num1 + num2}' + (' - even' if (num1 + num2) % 2 == 0 else ' - odd')
elif sign == '-':
    result = f'{num1} - {num2} = {num1 - num2}' + (' - even' if (num1 - num2) % 2 == 0 else ' - odd')
elif sign == '*':
    result = f'{num1} * {num2} = {num1 * num2}' + (' - even' if (num1 * num2) % 2 == 0 else ' - odd')
elif num2 == 0:
    result = f'Cannot divide {num1} by zero'
elif sign == '/':
    result = f'{num1} / {num2} = {num1 / num2:.2f}'
elif sign == '%':
    result = f'{num1} % {num2} = {num1 % num2}'

print(result)
