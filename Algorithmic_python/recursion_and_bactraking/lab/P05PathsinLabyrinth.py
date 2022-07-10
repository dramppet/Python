def find_path(row, col, lab, path, direction):

    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return

    if lab[row][col] == 'e':
        pass
    if lab[row][col] == '*':
        return

    find_path(row, col + 1, lab, 'R', direction)
    find_path(row, col - 1, lab, 'L', direction)
    find_path(row + 1, col, lab, 'D', direction)
    find_path(row - 1, col, lab, 'U', direction)

row = int(input())
col = int(input())

lab = []

for _ in range(row):
    lab.append(list(input()))

find_path(0, 0, lab,'',[])
