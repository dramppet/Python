first = input().split()
second = input().split()

rows = len(first) + 1
cols = len(second) + 1

dp = []

[dp.append([0] * cols) for _ in range(cols)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1] + 1
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
row = rows - 1
col = cols - 1

print(dp[rows - 1][cols - 1])
