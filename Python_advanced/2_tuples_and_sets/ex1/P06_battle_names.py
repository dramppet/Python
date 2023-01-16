count_name = int(input())

sum_name = 0
odd_sum = set()
even_sum = set()

for idx in range(1, count_name + 1):
    name = input()

    for ch in name:
        sum_name += int(ord(ch))
    after = sum_name // idx

    if after % 2 == 0:
        even_sum.add(after)
    else:
        odd_sum.add(after)
    sum_name = 0

if sum(even_sum) == sum(odd_sum):
    print(", ".join(str(x) for x in even_sum.union(odd_sum)))
if sum(odd_sum) > sum(even_sum):
    print(", ".join([str(x) for x in odd_sum.difference(even_sum)]))
else:
    print(", ".join([str(x) for x in even_sum.symmetric_difference(odd_sum)]))




