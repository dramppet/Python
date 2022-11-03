NYLON = 1.50
PAINT = 14.50
THINNER = 5.00

need_nylon = int(input())
need_paint = int(input())
col_thinner = int(input())
hours = int(input())

all_nylon = (need_nylon + 2) * NYLON
all_paint = (need_paint + (need_paint * 0.1)) * PAINT
all_thinner = col_thinner * THINNER
all_materials = all_nylon + all_paint + all_thinner + 0.4

sum_maistory = (all_materials * 0.3) * hours
final_sum = all_materials + sum_maistory

print(final_sum)