rows, cols = list(map(int,input().split(', ')))

matrix = []
sum_matrix_elements = 0

for _ in range(rows):
    elements_matrix = [int(x) for x in input().split(', ')]
    sum_matrix_elements += sum(elements_matrix)
    matrix.append(elements_matrix)

print(sum_matrix_elements)
print(matrix)