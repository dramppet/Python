MAX_CAPACITY = 255

num = int(input())

capacity = 0

for _ in range(num):
    cap = int(input())
    if cap + capacity > MAX_CAPACITY:
        print(f'Insufficient capacity!')
        continue
    capacity += cap

print(capacity)
