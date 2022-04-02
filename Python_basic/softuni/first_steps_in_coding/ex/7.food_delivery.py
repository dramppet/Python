CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15

count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegan_menu = int(input())

price_chicken_menu = count_chicken_menu * CHICKEN_MENU
price_fish_menu = count_fish_menu * FISH_MENU
price_vegan_menu = count_vegan_menu * VEGAN_MENU

all_menu = price_chicken_menu + price_fish_menu + price_vegan_menu

price_dessert = all_menu * 0.2

all_porachka = price_dessert + all_menu + 2.5

print(all_porachka)