day = int(input())
hours = int(input())
minuts = int(input())
seconds = int(input())

hours_day = hours + (day * 24)
minuts_hours = minuts + (hours_day * 60)
seconds_min = seconds + (minuts_hours * 60)

print(seconds_min)