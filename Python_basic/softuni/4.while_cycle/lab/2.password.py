username = input()
password = input()

data = input()

while not data == password:
    data = input()

print(f'Welcome {username}!')