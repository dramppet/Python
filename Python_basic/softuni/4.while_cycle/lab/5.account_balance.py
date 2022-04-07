input_line = input()
balance = 0

while not input_line == 'NoMoreMoney':
    amount = float(input_line)
    if amount < 0:
        print('Invalid operation!')
        break
    balance += amount
    print(f'Increase: {amount:.2f}')
    input_line = input()
print(f'Total: {balance:.2f}')