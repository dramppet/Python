MAX_STEPS = 10000
steps_walk = 0

while steps_walk < MAX_STEPS:
    steps = input()

    if steps == 'Going home':
        steps_walk += int(input())
        break
    steps_walk += int(steps)

if steps_walk >= MAX_STEPS:
    print("Goal reached! Good job!")
    print(f'{steps_walk - MAX_STEPS} steps over the goal!')
else:
    print(f'{MAX_STEPS - steps_walk} more steps to reach goal.')