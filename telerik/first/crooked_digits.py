number = input()

result = 0

for x in number:
    if x == '-' or x == '.':
        continue
    result += int(x)

while result > 9:
    temp = 0
    while result != 0:
        temp += result %10
        result //= 10
    result = temp
print(result)