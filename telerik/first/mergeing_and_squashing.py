count_number = int(input())

number_list = []

for _ in range(count_number):
    number_list.append(input())

merge_list = []
squash_list = []


def merge(f, s):
    first_str = str(f)
    second_str = str(s)

    return f'{first_str[1]}{second_str[0]}'


def squash(f, s):
    first_str = str(f)
    second_str = str(s)

    sum_num = int(first_str[1]) + int(second_str[0])

    sum_str = str(sum_num)[1] if sum_num > 9 else str(sum_num)

    return f'{first_str[0]}{sum_str}{second_str[1]}'


for idx in range(len(number_list) - 1):
    first = number_list[idx]
    second = number_list[idx + 1]

    merge_list.append(merge(first, second))
    squash_list.append(squash(first, second))

print(' '.join(merge_list))
print(' '.join(squash_list))
