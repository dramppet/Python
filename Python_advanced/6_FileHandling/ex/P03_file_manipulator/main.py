import os
while True:
    command, *info = input().split("-")

    if command == "End":
        break

    if command == "Create":
        file = open(info[0],"w")
        file.close()
    elif command == "Add":
        with open(info[0], "a") as file:
            file.write(f"{info[1]}\n")
    elif command == "Replace":
        try:
            with open(info[0], "r") as file:
                text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(info[1],info[2])

            with open(info[0],"w") as file:
                file.write("".join(text))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(info[0])
        except FileNotFoundError:
            print("An error occurred")