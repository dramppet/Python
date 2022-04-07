need_trip_money = float(input())
now_money = float(input())

spend_money_counter = 0
go_holiday = False
counter_day = 0

while spend_money_counter < 5:
    command = input()
    money = float(input())
    if command == 'spend':
        spend_money_counter += 1
        now_money -= money
        if now_money < 0:
            now_money = 0

    if command == 'save':
        now_money += money

    counter_day += 1
    if now_money >= need_trip_money:
        go_holiday = True
        break


if go_holiday:
    print(f'You saved the money for {counter_day} days.')
else:
    print(f"You can't save the money.")
    print(counter_day)

