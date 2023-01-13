numbers_students = int(input())
students_grades = {}

for _ in range(numbers_students):
    name, grade = input().split()
    grades = float(grade)

    if name not in students_grades:
        students_grades[name] = [grades]
    else:
        students_grades[name].append(grades)

for key,grades in students_grades.items():
    sum_value = sum(grades)/ len(grades)
    grade_str = ' '.join(str(f'{x:.2f}') for x in grades)
    print(f"{key} -> {grade_str} (avg: {sum_value:.2f})")
