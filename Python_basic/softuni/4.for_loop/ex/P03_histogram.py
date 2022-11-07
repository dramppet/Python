count_num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(count_num):
    num = int(input())

    if num < 200:
        p1 +=1
    elif num <= 399:
        p2 += 1
    elif num <= 599:
        p3 += 1
    elif num <= 799:
        p4 += 1
    else:
        p5 += 1

print(f'{p1 / count_num * 100 :.2f}%')
print(f'{p2 / count_num * 100 :.2f}%')
print(f'{p3 / count_num * 100 :.2f}%')
print(f'{p4 / count_num * 100 :.2f}%')
print(f'{p5 / count_num * 100 :.2f}%')
