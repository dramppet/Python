CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEG_MENU = 8.15

count_chicken_menu = int(input())
count_fish_menu = int(input())
count_veg_menu = int(input())

price_chicken = count_chicken_menu * CHICKEN_MENU
price_fish = count_fish_menu * FISH_MENU
price_veg = count_veg_menu * VEG_MENU
all_menu = price_chicken + price_fish + price_veg

price_dessert = all_menu * 0.2

all_delivery = all_menu + price_dessert + 2.5

print(round(all_delivery,2))