n, m = [int(el) for el in input().split(' ')]

people_r, people_c = 0,0

matrix = []

for row in range(n):
    row_element = input().split()
    for col in range(m):
        if row_element[col] == 'B':
            people_r, people_c = row, col
    matrix.append(row_element)

count_touched_opponents = 0
steps = 0
row = people_r
col = people_c

while True:
    command = input()
    if command == 'Finish':
        break
    if command == 'up':
        row -= 1
    elif command == 'down':
        row +=1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1
    if not(0 <= row < n and 0 <= col < m):
        row, col = people_r, people_c
        continue
    if matrix[row][col] == 'O':
        row, col = people_r, people_c
        continue
    if matrix[row][col] == 'P':
        count_touched_opponents += 1
        matrix[row][col] = '-'
    people_r = row
    people_c = col
    matrix[row][col] = 'B'
    steps += 1
    if count_touched_opponents == 3:
        break

print('Game over!')
print(f"Touched opponents: {count_touched_opponents} Moves made: {steps}")



