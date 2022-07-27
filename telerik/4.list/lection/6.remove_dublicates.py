input_list = input().split(',')

print_list = []

for x in range(len(input_list) - 1):
    for j in range(x+1,len(input_list) - 1):
        if input_list[x] != input_list[j]:
             print_list.append(input_list[x])

print_list.append(input_list[len(input_list) - 1])
print(*print_list,sep=',')