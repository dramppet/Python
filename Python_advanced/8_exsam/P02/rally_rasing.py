def create_matrix(size):
    matrix = []

    for _ in range(size):
        data = input().split(" ")
        matrix.append(data)
    return matrix


def game_logic(matrix):
    car_coordinates = [0, 0]
    up_tunel, down_tunel = [(r, matrix[r].index("T"))for r in range(len(matrix)) if "T" in matrix[r]]
    distance = 0
    finish_condition = True

    while True:
        command = input()

        if command == 'End':
            break
        elif command == 'down':
            pass
        elif command == "up":
            pass
        elif command == "left":
            pass
        elif command == "right":
            pass


size = int(input())
car_number = input()

matrix = create_matrix(size)

