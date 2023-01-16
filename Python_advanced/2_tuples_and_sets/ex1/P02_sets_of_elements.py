first,second = input().split()
n= int(first)
m= int(second)

set_n = {input() for _ in range(n)}
set_m = {input() for _ in range(m)}

print('\n'.join(set_n.intersection(set_m)))