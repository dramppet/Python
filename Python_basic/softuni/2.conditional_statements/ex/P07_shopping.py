budget = float(input())
count_videocard = int(input())
count_procesor = int(input())
count_ram = int(input())

sum_videocard = count_videocard * 250
sum_procesor = count_procesor * (sum_videocard * 0.35)
sum_ram = count_ram * (sum_videocard * 0.1)
all_sum = sum_videocard + sum_procesor + sum_ram


if count_videocard > count_procesor:
    all_sum *= 0.85

if budget >= all_sum:
    print(f'You have {budget - all_sum:.2f} leva left!')
else:
    print(f'Not enough money! You need {all_sum - budget:.2f} leva more!')

