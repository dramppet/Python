data = input().split()
avg_temp = int(input())
rain = int(input())
winter_length = int(input())

OPT_TEMP = 20
OPT_RAIN = 30
vis_god = False

days = int(data[0])
month = data[1]
year = int(data[2])

days += winter_length // 7

if year % 4 == 0:
    avg_temp += 5
    vis_god = True
if avg_temp > OPT_TEMP:
    days -= avg_temp - OPT_TEMP
else:
    days += OPT_TEMP - avg_temp
if OPT_RAIN > rain:
    rain_a = (OPT_RAIN - rain) // 3
    days += rain_a
else:
    rain_a = (rain - OPT_RAIN) // 3
    days += rain_a


if vis_god:
    if days < 0:
        print(f'{29 - abs(days)} February {year}')
    else:
        if days > 31:
            print(f'{days - 31} April {year}')
        else:
            if days == 0:
                print(f'29 February {year}')
            else:
                print(f'{days} March {year}')
else:
    if days < 0:
        print(f'{28 - abs(days)} February {year}')
    else:
        if days > 31:
            print(f'{days - 31} April {year}')
        else:
            print(f'{days} March {year}')


