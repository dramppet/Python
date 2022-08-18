n = float(input())

if n == 0:
    print("zero")
elif n >= 0 and n <= 1:
    print('small positive')
elif 0 <= n <= 1000000:
    print('positive')
elif n > 1000000:
    print('large positive')
elif n < 0 and n > -1:
    print('small negative')
elif n < - 1000000:
    print('large negative')
else:
    print('negative')
