n = int(input())
k = int(input())

sum_n = 1
sum_k = 1

for n_fac in range(1,n+1):
    sum_n *= n_fac

for k_fac in range(1,k+1):
    sum_k *= k_fac

print(sum_n//sum_k)