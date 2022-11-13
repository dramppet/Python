count_group = int(input())
count_night = int(input())
map_tran = int(input())
tic_musei = int(input())

all_night = count_night * 20
all_tran = map_tran * 1.60
all_musei = tic_musei * 6

all_sum_ane = all_night + all_tran + all_musei
all_group = (count_group * all_sum_ane) * 1.25

print(f'{all_group:.2f}')
