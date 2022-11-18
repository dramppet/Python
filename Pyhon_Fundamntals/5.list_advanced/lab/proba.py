nums = input().split()

# num = [int(el) for el in nums]
num = list(map(lambda x : int(x),nums))

# num_fil = [n for n in num if n %2 == 0]
num_fil = list(filter(lambda n: n%2 == 0,num))

print(num_fil)