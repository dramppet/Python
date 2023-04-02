budget = int(input())
standard_price = int(input())
discount_per_purchase = int(input())
price_threshold = int(input())

socks_count = 0

if budget - standard_price - price_threshold >= 0:
    socks_count += 1
    budget -= standard_price

while budget > 0:
    standard = abs(standard_price - (discount_per_purchase * socks_count))

    if budget - standard < 0:
        break

    if standard > price_threshold:
        budget -= standard
    else:
        budget-= price_threshold

    socks_count += 1

    if budget - price_threshold < 0:
        break

if socks_count >= 10:
    socks_count += 1

print(f"{socks_count},{abs(budget):.0f}")