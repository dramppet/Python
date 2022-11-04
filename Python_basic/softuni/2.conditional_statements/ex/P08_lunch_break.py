from math import ceil
name_serial = input()
time_serial = int(input())
time_break = int(input())

time_lunch = time_break * 1 / 8
time_otdix = time_break * 1/4
time_out = int(ceil(time_break - time_lunch - time_otdix))

if  time_out >= time_serial:
    print(f'You have enough time to watch {name_serial} '
          f'and left with {time_out - time_serial} minutes free time."')
else:
    print(f"You don't have enough time to watch {name_serial}, "
          f"you need {time_serial - time_out} more minutes.")