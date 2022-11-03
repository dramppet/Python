year_tax = int(input())

price_kecove = year_tax - (year_tax * 0.4)
price_ekip = price_kecove - (price_kecove * 0.2)
price_topka = price_ekip / 4
price_aksesoary = price_topka / 5

all_price = year_tax + price_kecove + price_ekip + price_topka + price_aksesoary

print(all_price)