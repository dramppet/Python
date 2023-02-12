rows = int(input())

matrix = [ [int(el) for el in input().split(", ")]for _ in range(rows)]

primary_diagonal = [matrix[row][row] for row in range(len(matrix))]

secondary_diagonal =[matrix[row][len(matrix) - row - 1] for row in range(len(matrix) - 1, - 1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal][::-1])}. Sum: {sum(secondary_diagonal)}")