age = int(input())
price_washing_machine = float(input())
price_one_toy = int(input())

toy_count = 0
price = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        price += (10 * i) / 2 - 1
    else:
        toy_count+=1

price += toy_count * price_one_toy

if price >= price_washing_machine:
    print(f'Yes! {price - price_washing_machine:.2f}')
else:
    print(f'No! {price_washing_machine - price:.2f}')

