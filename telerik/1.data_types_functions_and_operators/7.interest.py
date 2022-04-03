deposit_money = int(input())

first_year = deposit_money + (deposit_money * 0.05)
second_year = first_year + (first_year * 0.05)
three_year = second_year + (second_year * 0.05)

print(f'{first_year:.2f}')
print(f'{second_year:.2f}')
print(f'{three_year:.2f}')