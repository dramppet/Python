count_rows = int(input())

# matrix = [[int(el) for el in input().split(", ")]for _ in range(count_rows)]
# matrix_comp = [num for row in matrix for num in row]
#
# m = []
# for row in matrix:
#     for col in row:
#         m.append(col)
#
# print(matrix_comp)

matrix = []

for _ in range(count_rows):
    row = [int(x) for x in input().split(", ")]
    matrix.extend(row)

print(matrix)