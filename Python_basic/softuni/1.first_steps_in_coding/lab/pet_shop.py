count_food_dog = int(input())
count_food_cat = int(input())

ONE_FOD_PRICE_DOGS = 2.50
ONE_FOD_PRICE_CAT = 4

price_all_dog = count_food_dog * ONE_FOD_PRICE_DOGS
price_all_cat = count_food_cat * ONE_FOD_PRICE_CAT

all_price = price_all_dog + price_all_cat

print(f'{all_price} lv.')


