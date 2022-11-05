count_num = int(input())

even_sum = 0
odd_sum = 0

for i in range(count_num):
    if i % 2 == 0:
        even_sum += int(input())
    else:
        odd_sum += int(input())

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')