deposit_sum = float(input())
term_deposit = int(input())
year_percent = float(input())

lixva = deposit_sum * (year_percent /100 )
lixva_for_one_mounth = lixva / 12
all_sum = deposit_sum + (term_deposit * lixva_for_one_mounth)


print(all_sum)