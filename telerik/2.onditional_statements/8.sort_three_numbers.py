first = int(input())
second = int(input())
three = int(input())

if first > second and first > three:
    if second > three:
        print(f'{first} {second} {three}')
    else:
        print(f'{first} {three} {second}')
elif second > first and second > three:
    if first > three:
        print(f'{second} {first} {three}')
    else:
        print(f'{second} {three} {first}')
else:
    if first > second:
        print(f'{three} {first} {second}')
    else:
        print(f'{three} {second} {first}')