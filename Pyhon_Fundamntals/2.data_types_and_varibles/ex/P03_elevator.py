import math

count_person = int(input())
capacity = int(input())

course = math.ceil(count_person / capacity)

if course <= capacity:
    print(course)
else:
    print(course)