count_list = int(input())

is_sorted = True

for _ in range(count_list):
    next_list = [int(x) for x in input().split(',')]

    for x in range(len(next_list) - 1):
        if next_list[x] >= next_list[x+1]:
            is_sorted = False
            break

    if is_sorted:
       print('true')
    else:
       print('false')

