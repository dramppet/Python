count = int(input())

list_guest = {input() for _ in range(count)}

while True:
    command = input()

    if command == "END":
        break

    if command in list_guest:
        list_guest.remove(command)

print(len(list_guest))
for name in sorted(list_guest):
    print(name)
