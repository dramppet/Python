employees_happiness = input().split()
factor = int(input())

multiply_emp = [int(x) * factor for x in employees_happiness]
avg_emp = sum(multiply_emp) // len(multiply_emp)

happy_emp = list(filter(lambda x: x> avg_emp,multiply_emp))
avg_employee_happy = len(multiply_emp) // 2
if len(happy_emp)>= avg_employee_happy:
    print(f"Score: {len(happy_emp)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f'Score: {len(happy_emp)}/{len(employees_happiness)}. Employees are not happy!')


# employees = list(map(lambda x: int(x) * factor,employees_happiness))
# filtered_emp = list(filter(lambda x: x >= (sum(employees) / len(employees_happiness)),employees_happiness))