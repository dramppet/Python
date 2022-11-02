PRICE_DOG_FOOD = 2.50
PRICE_CAT_FOOD = 4.00

count_food_dogs = int(input())
count_food_cats = int(input())

all_price = (count_food_dogs * PRICE_DOG_FOOD) + (count_food_cats * PRICE_CAT_FOOD)

print(f'{all_price} lv.')