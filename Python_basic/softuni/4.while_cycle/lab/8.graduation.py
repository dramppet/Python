name_student = input()

year = 1
sum_grade = 0
fail_grade = 0
fail = True
while year <= 12:
    if fail_grade > 1:
        fail = False
        break
    grade = float(input())

    if grade < 4:
        fail_grade +=1
        continue

    sum_grade += grade
    year +=1

if fail:
    avg_grade = sum_grade / 12
    print(f'{name_student} graduated. Average grade: {avg_grade:.2f}')
else:
    print(f'{name_student} has been excluded at {year} grade')