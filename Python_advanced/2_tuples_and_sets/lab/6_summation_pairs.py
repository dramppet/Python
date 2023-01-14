numbers = list(map(int,input().split()))
find_numbers = int(input())
numbers_set = set()

for i in range(len(numbers)):
    for j in range(i + 1,len(numbers)):
        if numbers[i] + numbers[j] == find_numbers:
            numbers_set.add(f"{numbers[i]} + {numbers[j]} == {find_numbers}")

for n in numbers_set:
    print(n)