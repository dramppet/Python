rows = int(input())
cols = int(input())

matrix = []
dp = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    dp.append([0] * cols)

dp[0][0] = matrix[0][0]

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1]  + matrix[0][col]

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        dp[row][col] = max(dp[row - 1][col],dp[row][col - 1]) + matrix[row][col]

for row in dp:
    print(row)