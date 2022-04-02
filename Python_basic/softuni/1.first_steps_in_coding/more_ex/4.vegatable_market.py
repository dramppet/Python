ONE_EURO = 1.94

price_kg_veg = float(input())
price_kg_fr = float(input())
all_kg_veg = int(input())
all_kg_fr = int(input())

veg  = price_kg_veg * all_kg_veg
frut = price_kg_fr * all_kg_fr

all_price = (veg +frut) / ONE_EURO

print(f'{all_price:.2f}')
