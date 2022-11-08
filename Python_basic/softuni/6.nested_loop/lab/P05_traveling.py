spend_money = 0

while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())

    while True:
        price = float(input())
        spend_money += price
        if spend_money >= budget:
            print(f'Going to {destination}!')
            spend_money = 0
            break
