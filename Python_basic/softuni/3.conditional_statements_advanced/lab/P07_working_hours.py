hours_of_day = int(input())
day_of_week = input()

if hours_of_day >= 10 and hours_of_day <= 18:
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week =="Wednesday" or day_of_week ==" Thursday" or day_of_week == "Friday":
        print("open")
    else:
        print("closed")
else:
    print("closed")