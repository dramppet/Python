price_teniska = float(input())
price_info = float(input())

price_6orti = price_teniska * 0.75
price_4orapi = price_6orti * 0.2
price_butonki = (price_teniska + price_6orti) * 2
all_sum = price_teniska + price_6orti + price_4orapi + price_butonki
all_sum_ost = all_sum * 0.85

if all_sum_ost >= price_info:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {all_sum_ost:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {abs(price_info - all_sum_ost):.2f} lv. more.')
