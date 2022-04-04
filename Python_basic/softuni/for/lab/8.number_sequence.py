import sys

count_number = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for _ in range(count_number):
    n = int(input())

    if n > max_number:
        max_number = n

    if n < min_number:
        min_number = n

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

