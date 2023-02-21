def create_matrix(size):
    matrix = []

    for _ in range(size):
        data = input().split(" ")
        matrix.append(data)
    return matrix


def game_logic(matrix):
    car_coordinates = [0, 0]
    up_tunel, down_tunel = [(r, matrix[r].index("T")) for r in range(len(matrix)) if "T" in matrix[r]]
    distance = 0
    finish_condition = False

    while True:
        command = input()

        if command == 'End':
            matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
            return matrix, distance, finish_condition
        elif command == 'down':
            car_coordinates[0] += 1
        elif command == "up":
            car_coordinates[0] -= 1
        elif command == "left":
            car_coordinates[1] -= 1
        elif command == "right":
            car_coordinates[1] += 1

        if matrix[car_coordinates[0]][car_coordinates[1]] == 'T':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'
            if tuple(car_coordinates) == up_tunel:
                matrix[down_tunel[0]][down_tunel[1]] = '.'
                car_coordinates = [down_tunel[0], down_tunel[1]]
            else:
                matrix[up_tunel[0]][up_tunel[1]] = '.'
                car_coordinates = [up_tunel[0], up_tunel[1]]

            distance += 30
            continue
        elif matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            finish_condition = True
            distance += 10
            matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
            return matrix, distance, finish_condition

        distance += 10


def print_func(data, rasing_number):
    matrix, distance, finish_cond = data

    if finish_cond:
        print(f"Racing car {rasing_number} finished the stage!")
    else:
        print(f'Racing car {rasing_number} DNF.')

    print(f'Distance covered {distance} km.')

    [print(*r,sep='') for r in matrix]


size = int(input())
car_number = input()

matrix = create_matrix(size)
print_func(game_logic(matrix), car_number)
