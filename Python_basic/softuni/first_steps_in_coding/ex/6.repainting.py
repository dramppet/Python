PREDPAZEN_NA = 1.50
PAINT = 14.50
RAZREDITEL = 5.00

need_nylon= int(input())
need_paint = int(input())
kol_raz = int(input())
hours_maistors = int(input())

sum_nylon = (need_nylon + 2) * PREDPAZEN_NA
sum_paint = (need_paint + (need_paint * 10 /100)) * PAINT
sum_razreditel = kol_raz * RAZREDITEL
sum_toba = 0.40

sum_mat = sum_nylon +sum_paint +sum_razreditel + sum_toba

sum_maistori = (sum_mat * 30/100) * hours_maistors

final_sum = sum_mat + sum_maistori

print(final_sum)