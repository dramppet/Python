sum_deposit = float(input())
count_deposit = int(input())
year_procent = float(input())

cont_lixva = sum_deposit * (year_procent / 100)
lixva_for_one_mount = cont_lixva / 12
all_sum = sum_deposit + (count_deposit * lixva_for_one_mount)

print(all_sum)