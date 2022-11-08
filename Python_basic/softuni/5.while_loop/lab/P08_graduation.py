name = input()

sum_grade = 0
count = 0
wrong_grade = 0

while True:
    count += 1
    if count > 12 or wrong_grade == 2:
        break
    grade = float(input())

    if grade < 4.00:
        wrong_grade += 1
        continue

    sum_grade += grade

if wrong_grade < 2:
    print(f'{name} graduated. Average grade: {sum_grade / 12:.2f}')
else:
    print(f'{name} has been excluded at {count - 2} grade')