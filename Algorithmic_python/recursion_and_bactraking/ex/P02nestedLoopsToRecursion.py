def gen_vector(idx,vector,n):
    if idx >= len(vector):
        print(*vector)
        return

    for num in range(1,n + 1):
        vector[idx] = num

        gen_vector(idx + 1,vector,n)

n = int(input())

arr = [None] * n

gen_vector(0, arr, n)