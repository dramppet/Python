max_num = int(input())

sum_n = 0

while True:
    sum_n = 2*sum_n + 1
    if sum_n <= max_num:
        print(sum_n)
    else:
        break