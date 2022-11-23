diff1 = [int(x) for x in input().split()]
diff2 = [int(x) for x in input().split()]

count = 0

while True:
    if len(diff1) <= count and len(diff2) <= count:
        break


    if len(diff1) <= count:
        print(f'- x {diff2[count]}')
    if len(diff2) <= count:
        print(f'- {diff1[count]} x')
    if len(diff1) > count and len(diff2) > count:
        if diff1[count] == diff2[count]:
            print(f'+ {diff1[count]} {diff2[count]}')
        else:
            print(f'- {diff1[count]} {diff2[count]}')




    count += 1
