hour = int(input())
minutes = int(input())

minutes_add = minutes + 15

if minutes_add > 59:
    hour += 1
    if hour > 23:
        hour = hour - 24
    minutes = minutes_add - 60
else:
    minutes = minutes_add


if minutes < 10:
    print(f'{hour}:0{minutes}')
else:
    print(f'{hour}:{minutes}')
