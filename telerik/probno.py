import sys

count_horse = int(input())

horse = []

for _ in range(count_horse):
    single_horse = int(input())
    horse.append(single_horse)


int_min = sys.maxsize
power = 0

for x in range(len(horse)):
    first = horse[x]
    next_x = x + 1
    for next_x in range(next_x,len(horse)):
        second = horse[next_x]
        power = abs(first - second)

        if power < int_min:
            int_min = power

print(int_min)