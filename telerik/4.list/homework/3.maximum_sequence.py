input = [int(x) for x in input().split(' ')]

seq = 1
max_seq = 0

for n in range(0,len(input) - 1):
    first = input[n]
    second = input[n + 1]
    if first == second:
       seq+=1
    else:
        seq = 0

    if seq > max_seq:
        max_seq = seq

print(max_seq)