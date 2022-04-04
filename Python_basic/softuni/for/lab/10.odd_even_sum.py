count_numbers = int(input())

sum_even = 0
sum_odd = 0

for i in range(count_numbers):
    n = int(input())

    if i % 2 == 0:
        sum_even += n
    else:
        sum_odd += n

if sum_even == sum_odd:
    print('Yes')
    print('Sum =',sum_odd)
else:
    print('No')
    print(f'Diff = {abs(sum_odd - sum_even)}')