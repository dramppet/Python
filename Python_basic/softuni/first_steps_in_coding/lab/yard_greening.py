kv_m = float(input())

price = kv_m * 7.61

ost = price * 0.18
sum_final = price - ost

print(f'The final price: {sum_final} lv.')
print(f'The discount is: {ost} lv.')