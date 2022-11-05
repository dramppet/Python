count_num = int(input())

left_sum = 0

for _ in range(count_num):
    left_sum += int(input())

right_sum = 0

for _ in range(count_num):
    right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')