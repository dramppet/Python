import sys

count_number = int(input())

first = int(input())
second = int(input())
third = int(input())

max_number = -sys.maxsize
avg_number = -sys.maxsize
min_number = -sys.maxsize

if first >= second and first >= third:
    max_number = first
    if second >= third:
        avg_number = second
        min_number = third
    else:
        avg_number = third
        min_number = second
elif second >= first and second >= third:
    max_number = second
    if first >= third:
        avg_number = first
        min_number = third
    else:
        avg_number = third
        min_number = first
else:
    max_number = third
    if first >= second:
        avg_number = first
        min_number = second
    else:
        avg_number = second
        min_number = first

for _ in range(3,count_number):

    num = int(input())

    if num >= max_number:
        min_number = avg_number
        avg_number = min_number
        max_number = num

    if num >= avg_number:
        min_number = avg_number
        avg_number = num

    if num >= min_number:
        min_number = num


print(f'{max_number}, {avg_number} and {min_number}')
