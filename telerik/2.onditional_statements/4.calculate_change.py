price = float(input())
custom_price = float(input())

price_return = custom_price - price

leva = price_return % 1.0
print(leva)