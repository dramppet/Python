numbers = [int(x) for x in input().split()]

count = 0

for num in numbers:
    if num % 3 == 0 and num % 7 == 0:
        count += num

count_num = 0
for d,num in enumerate(str(count)):
    count_num += int(num)

print(count_num)