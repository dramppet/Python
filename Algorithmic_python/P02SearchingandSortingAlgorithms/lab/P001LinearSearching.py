def binary_searched(n, target):
    for idx, num in enumerate(n):
        if num == target:
            return idx

n = [int(x) for x in input().split()]

serched_element = int(input())

print(binary_searched(n,serched_element))