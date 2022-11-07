count = input()
sum_count = 0
while count != 'NoMoreMoney':
    num = float(count)
    if num >= 0:
        sum_count += num
        print(f'Increase: {num:.2f}')
    else:
        print('Invalid operation!')
        break
    count = input()
print(f'Total: {sum_count:.2f}')