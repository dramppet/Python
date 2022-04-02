year_taxi_basket = int(input())

price_kecove = year_taxi_basket - (year_taxi_basket * 0.4)
price_ekip = price_kecove - (price_kecove * 0.2)
price_topka = 1/4 * price_ekip
price_aksesoar = 1/5 * price_topka

all_price = price_kecove + price_ekip + price_topka + price_aksesoar + year_taxi_basket

print(all_price)