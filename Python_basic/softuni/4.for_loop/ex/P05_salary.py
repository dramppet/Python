count_open_tab = int(input())
salary = int(input())

for _ in range(count_open_tab):
    tabs = input()

    if tabs == 'Facebook':
        salary -= 150
    elif tabs == 'Instagram':
        salary -= 100
    elif tabs == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print('You have lost your salary.')

