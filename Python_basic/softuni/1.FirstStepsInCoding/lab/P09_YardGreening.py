PRICE_ONE_KVM = 7.61
DISCOUNT_PERCENT = 18.0

need_metri = float(input())

price_need = need_metri * PRICE_ONE_KVM
discount_price = price_need * (DISCOUNT_PERCENT / 100)

price = price_need - discount_price

print(f'The final price is: {price} lv.')
print(f'The discount is: {discount_price} lv.')