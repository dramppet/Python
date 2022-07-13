first_list = [int(x) for x in input().split(',')]
second_list = [int(x) for x in input().split(',')]

combine_list = []
range_new_list = len(first_list) + len(second_list)

position = 0
for x in range(range_new_list):
    if x % 2 == 0:
        combine_list.append(first_list[position])
    else:
        combine_list.append(second_list[position])
        position+=1

print(*combine_list,sep=',')

