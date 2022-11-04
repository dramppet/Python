time_first = int(input())
time_second = int(input())
time_third = int(input())

all_time = time_first + time_second + time_third

minutes = all_time // 60
second = all_time % 60

if second < 10:
    print(f'{minutes}:0{second}')
else:
    print(f'{minutes}:{second}')