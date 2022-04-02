PAKEG_PEN  = 5.80
PAKEG_MARKER = 7.2
PREPARAT = 1.2

count_packeg_pen = int(input())
count_packeg_marker = int(input())
litri_preparat = int(input())
procent_namalenie = int(input())

price_pakeg_pen = count_packeg_pen * PAKEG_PEN
price_pakeg_marker = count_packeg_marker * PAKEG_MARKER
price_preparat = litri_preparat * PREPARAT
price_all = price_pakeg_pen + price_pakeg_marker + price_preparat

price_ost = price_all - (price_all * procent_namalenie / 100)

print(price_ost)