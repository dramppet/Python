bank_acc = input()
total_acc  = 0

while not bank_acc == 'NoMoreMoney':
    com = float(bank_acc)
    if com < 0:
        print('Invalid operation!')
        break
    print('Increase: ',com)
    total_acc += com
    bank_acc = input()
print(f'Total:{total_acc:.2f}')