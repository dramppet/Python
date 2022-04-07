failed_thresold = int(input())

filed_times = 0
solved_problems = 0
grade_sum = 0
last_problem = ''
has_failed = True

while filed_times < failed_thresold:
    problem_name = input()

    if problem_name == 'Enough':
        has_failed = False
        break

    grades = int(input())
    if grades <= 4:
        filed_times += 1

    grade_sum += grades
    solved_problems += 1
    last_problem = problem_name

if has_failed:
    print(f'You need a break, {failed_thresold} poor grades.')
else:
    print(f'Average score: {grade_sum / solved_problems:.2f}')
    print(f'Number of problems: {solved_problems}')
    print(f'Last problem: {last_problem}')



