zoo = []
for _ in range(3):
    data = input()
    zoo.append(data)

print(zoo)

zoo[0],zoo[1],zoo[2] = zoo[2],zoo[1],zoo[0]

print(zoo)