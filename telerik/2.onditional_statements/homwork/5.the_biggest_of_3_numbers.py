first = float(input())
second = float(input())
three = float(input())

if first > second and first > three:
    print(first)
elif second > first and second > three:
    print(second)
else:
    print(three)

