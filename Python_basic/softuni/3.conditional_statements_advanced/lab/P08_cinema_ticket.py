day_of_week = input()
ticket = 0

if  day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
    ticket = 12
elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    ticket = 14
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    ticket = 16

print(ticket)