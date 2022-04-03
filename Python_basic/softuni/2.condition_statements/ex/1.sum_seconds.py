time_first = int(input())
time_second = int(input())
time_third = int(input())

all_sum = time_first + time_second + time_third

minutes = all_sum // 60
seconds = all_sum % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')