import sys
from functools import reduce

number_str = input()

first = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
second = int(number_str[0]) + int(number_str[1]) * int(number_str[2])
third = int(number_str[0]) * int(number_str[1]) + int(number_str[2])
four = int(number_str[0]) * int(number_str[1]) * int(number_str[2])

print(max(first,second,third,four))