exam_hour = int(input())
exam_minutes = int(input())

student_hour = int(input())
student_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
student_time_in_minutes = student_hour * 60 + student_minutes

time_diff = exam_time_in_minutes - student_time_in_minutes

if time_diff > 30:
    print('Early')
elif time_diff < 0:
    print('Late')
else:
    print('On time')

hours = 0
minutes = abs(time_diff)

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

result = ''

if hours > 0:
    result += str(hours) + ":" + ("0" + str(minutes) if minutes < 10 else str (minutes)) + " hours"
else:
    result += str(minutes) + " minutes"

if time_diff > 0:
    result += " before the start"
else:
    result += " after the start"


print(result)
