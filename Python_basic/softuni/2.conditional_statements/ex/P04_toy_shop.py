PUZZLE = 2.6
DOL = 3
TEDY_BEAR = 4.1
MINION = 8.2
TRUCK = 2

trip_price = float(input())
count_puzzle = int(input())
count_dol = int(input())
count_bear = int(input())
count_minion = int(input())
count_truck = int(input())

price_all_games = (count_puzzle * PUZZLE) + (count_dol * DOL) \
            + (count_bear * TEDY_BEAR) + (count_minion * MINION) \
            + (count_truck * TRUCK)


count_games = count_puzzle + count_dol + count_bear + count_minion + count_truck

if count_games >= 50:
    price_all_games -= price_all_games * 0.25

price_all_games -= price_all_games * 0.1



if  price_all_games >= trip_price:
    print(f'Yes! {(price_all_games - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - price_all_games):.2f} lv needed.')