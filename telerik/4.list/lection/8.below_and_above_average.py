input_list = [int(el) for el in input().split(',')]

sum_list = 0.0

for el in range(len(input_list)):
    sum_list += input_list[el]

avg = sum_list / len(input_list)

below = []
above = []

for n in range(len(input_list)):
    if input_list[n] > avg:
        above.append(input_list[n])
    else:
        below.append(input_list[n])

# print(f'{avg:.2f}')
# print(f"below: {*below,sep=','}")
# print(*above,sep=',')
