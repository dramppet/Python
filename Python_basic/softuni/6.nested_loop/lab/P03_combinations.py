n = int(input())

cobinations_count = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            product = x1 + x2 + x3

            if product == n:
                cobinations_count += 1

print(cobinations_count)
