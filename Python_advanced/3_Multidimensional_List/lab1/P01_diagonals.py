rows = int(input())

matrix = [ [int(el) for el in input().split(", ")]for _ in range(rows)]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]

