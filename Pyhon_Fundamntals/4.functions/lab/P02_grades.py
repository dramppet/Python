def type_of_grade(grade_input):
    if 2.00 <= grade_input <= 2.99:
        return 'Fail'
    elif 3.00 <= grade_input <= 3.49:
        return 'Poor'
    elif 3.50 <= grade_input <= 4.49:
        return 'Good'
    elif 4.50 <= grade_input <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_input <= 6.00:
        return 'Excellent'

grade = float(input())
print(type_of_grade(grade))