import math
series = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8
leisure_time = break_length / 4
time_taken = leisure_time + lunch_time + episode_length
time_left = break_length - time_taken

if  time_left >= 0:
    print(f'You have enough time to watch {series} '
          f'and left with {math.ceil(time_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, "
          f"you need {math.ceil(abs(time_left))} more minutes.")