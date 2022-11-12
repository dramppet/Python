line = input().split(' ')
numbers_list = list()

for num in line:
    if int(num) > 0:
        numbers_list.append(-int(num))
    else:
        numbers_list.append(abs(int(num)))

print(numbers_list)
