need_coffee = 0

while True:
    events = input()

    if events == 'END':
        break

    if events == 'coding':
        need_coffee += 1
    elif events == 'dog' or events == 'cat':
        need_coffee += 1
    elif events == 'movie':
        need_coffee += 1
    else:
        continue

    if events.islower():
        need_coffee += 1
    if events.isupper():
        need_coffee += 2

if need_coffee > 5:
    print('You need extra sleep')
else:
    print(need_coffee)


