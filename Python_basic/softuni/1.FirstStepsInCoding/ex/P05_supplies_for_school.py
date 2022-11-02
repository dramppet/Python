PAKET_PEN = 5.80
PAKET_MARKER = 7.20
PAKET_PREPARAT = 1.20

count_paket_pen = int(input())
count_paket_marker = int(input())
litri_preparat = int(input())
procent_discount = int(input())

price_pen = count_paket_pen * PAKET_PEN
price_marker = count_paket_marker * PAKET_MARKER
price_preparat = litri_preparat * PAKET_PREPARAT
all_price_material = price_pen + price_marker + price_preparat
prise_discount = all_price_material - (all_price_material * (procent_discount / 100))

print(prise_discount)