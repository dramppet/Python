first = input().split(',')
second = input().split(',')

min_list = min(len(first),len(second))

first_len = 0
second_len = 0
equal = 0

for char in range(min_list):
    if first[char] > second[char]:
        first_len += 1
    elif first[char] < second[char]:
        second_len += 1
    else:
        equal += 1

if first_len > second_len:
    print('First')
elif first_len < second_len:
    print('Second')
else:
    print('Equal')
