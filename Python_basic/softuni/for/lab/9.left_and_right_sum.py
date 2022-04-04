count_number = int(input())

sum_left = 0
sum_right = 0

for _ in range(count_number):
    n = int(input())
    sum_left += n

for _ in range(count_number):
    n = int(input())
    sum_right += n

if sum_left == sum_right:
    print('Yes, sum =',sum_left)
else:
    sum_left_right = sum_left - sum_right
    print('No, diff =',abs(sum_left_right))