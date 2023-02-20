SIZE = 6

players = input().split(", ")

matrix = [list(input().split()) for _ in range(SIZE)]

players_rest_data = {player: 0 for player in players}

while True:
    row, col = [int(x) for x in input().strip("()").split(", ")]

    if players_rest_data[players[0]] > 0:
        players_rest_data[players[0]] -= 1
        players[0], players[1] = players[1], players[0]
        continue

    position = matrix[row][col]

    if position == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break

    if position == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break

    if position == "W":
        print(f"{players[0]} hits a wall and needs to rest.")
        players_rest_data[players[0]] += 1

    players[0], players[1] = players[1], players[0]

