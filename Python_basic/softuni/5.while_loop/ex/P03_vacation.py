vacation_price = float(input())
balance = float(input())

days_spending = 0
days = 0

while days_spending < 5:
    action = input()
    money = float(input())

    days += 1

    if action == 'spend':
        balance = balance - money if balance - money > 0 else 0
        days_spending += 1
    elif action == 'save':
        balance += money
        days_spending = 0

    if balance >= vacation_price:
        print(f'You saved the money for {days} days.')
        break

else:
    print("You can't save the money.")
    print(f'{days}')


