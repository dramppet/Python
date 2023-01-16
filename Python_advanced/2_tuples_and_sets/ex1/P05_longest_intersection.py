import sys

count_line = int(input())

max_length = -sys.maxsize
max_set = set()

for _ in range(count_line):
    first, second = input().split('-')
    f_start, f_end = first.split(',')
    s_start, s_end = second.split(',')

    first_set = set(range(int(f_start),int(f_end) + 1))
    second_set = set(range(int(s_start),int(s_end) + 1))

    intersection_set = first_set.intersection(second_set)

    if len(intersection_set) > max_length:
        max_length = len(intersection_set)
        max_set = intersection_set

setts = ', '.join([str(x) for x in max_set])

print(f"Longest intersection is [{setts}] with length {max_length}")
