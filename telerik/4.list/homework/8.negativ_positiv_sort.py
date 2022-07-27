list_input = [int(x) for x in input().split(' ')]

list_positiv = []
list_negativ  = []

for n in range(len(list_input)):
    if list_input[n] > 0:
        list_positiv.append(list_input[n])
    else:
        list_negativ.append(list_input[n])

list_negativ.append(list_positiv)

print(' '.join(str(x) for x in list_negativ))