tip_projection = input()
count_rows = int(input())
count_columns = int(input())

income = 0

cinema_cap = count_columns * count_rows

if tip_projection == 'Premiere':
    income = cinema_cap * 12
elif tip_projection == 'Normal':
    income = cinema_cap * 7.5
else:
    income = cinema_cap * 5.00

print(f'{income:.2f} leva')

