def find_path(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return

    if lab[row][col] == 'e':
        return

    if lab[row][col] == '*':
        return

    if lab[row][col] == 'v':
        return

    lab[row][col] = 'v'
    path.append(direction)

    find_path(row, col + 1, lab, 'R', path)
    find_path(row, col - 1, lab, 'L', path)
    find_path(row + 1, col, lab, 'D', path)
    find_path(row - 1, col, lab, 'U', path)

    lab[row][col] = '-'


row = int(input())
col = int(input())

lab = []

for _ in range(row):
    lab.append(list(input()))

find_path(0, 0, lab, '', [])
