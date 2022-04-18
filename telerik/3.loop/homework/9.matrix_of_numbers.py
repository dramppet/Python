num_input = int(input())

for num in range(1,num_input + 1):
    for sec_num in range(num,num_input + 1):
       print(sec_num,end=' ')
    num_input +=1
    print()