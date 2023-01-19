rows = int(input())

# result = []
#
# for _ in range(rows):
#     row = [int(x) for x in input().split(', ')]
#     result.append([el for el in row if el % 2 == 0])
#
# print(result)

# comprehension

# matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
# print([x for x in row if x % 2 == 0] for row in matrix)