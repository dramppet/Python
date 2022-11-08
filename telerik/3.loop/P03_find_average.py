num = int(input())

num_count = 0

for _ in range(num):
    number = float(input())
    num_count += number

print(f'{num_count / num:.2f}')