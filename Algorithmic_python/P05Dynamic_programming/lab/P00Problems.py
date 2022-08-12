first = input()
second = input()

rows = len(first) + 1
cols  = len(second) + 1

dp= []

[dp.append([0] * cols) for _ in range(rows)]


