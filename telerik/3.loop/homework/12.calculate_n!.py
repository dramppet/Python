n = int(input())
k = int(input())

count_n = 1
count_k = 1

sum_n = 1
sum_k = 1

while True:

    if count_n > n and count_k > k:
        break

    if count_n < n + 1:
        sum_n *= count_n
        count_n+=1

    if count_k < k  + 1:
        sum_k *= count_k
        count_k+=1

print(sum_n // sum_k)
