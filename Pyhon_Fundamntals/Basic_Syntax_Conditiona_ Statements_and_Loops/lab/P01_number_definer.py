num = float(input())

if num == 0:
    print("zero")
elif num >= 0 and num <= 1:
    print('small positive')
elif 0 <= num <= 1000000:
    print('positive')
elif num > 1000000:
    print('large positive')
elif num < 0 and num > -1:
    print('small negative')
elif num < - 1000000:
    print('large negative')
else:
    print('negative')
