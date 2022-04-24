input_list = [int(x) for x in input().split(',')]

positive_list = []
negative_list = []

for el in range(len(input_list)):
    if input_list[el] < 0:
        negative_list.append(input_list[el])
    elif input_list[el] > 0:
        positive_list.append(input_list[el])
    else:
        positive_list.insert(0,input_list[el])


for pos_el in range(len(positive_list)):
    negative_list.append(positive_list[pos_el])


print(*negative_list,sep=',')

