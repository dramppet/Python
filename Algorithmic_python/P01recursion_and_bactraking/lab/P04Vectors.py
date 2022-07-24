def gen(idx,num):
    if idx >= len(num):
        print(*vector,sep='')
        return
    for nums in range(2):
        vector[idx] = nums
        gen(idx + 1, num)

n = int(input())
vector = [None] * n
gen(0,vector)
