clothes = [int(x) for x in input().split()]
rack_space = int(input())

rack_count = 1
current_rack_space = rack_space

while clothes:
    cloth = clothes.pop()
    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth
    else:
        rack_count += 1
        current_rack_space = rack_space - cloth
print(rack_count)

