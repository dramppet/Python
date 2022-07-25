rows = int(input())
cols = int(input())

matrix = []

for row in range(rows):
    line = input()
    matrix.append(line)

print(*matrix,sep=' ')