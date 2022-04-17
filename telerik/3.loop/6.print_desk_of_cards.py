cards_num = input()

if cards_num == 'J':
    cards_num = 11
if cards_num == 'Q':
    cards_num = 12
if cards_num == 'K':
    cards_num = 13
if cards_num == 'A':
    cards_num = 14


for num in range(2,int(cards_num) + 1):

    if num <= 10:
        print(f'{num} of spades',end=', ')
        print(f'{num} of clubs',end=', ')
        print(f'{num} of hearts',end=', ')
        print(f'{num} of diamonds')
    if num == 11:
        print(f'J of spades', end=', ')
        print(f'J of clubs', end=', ')
        print(f'J of hearts', end=', ')
        print(f'J of diamonds')
    if num == 12:
        print(f'Q of spades', end=', ')
        print(f'Q of clubs', end=', ')
        print(f'Q of hearts', end=', ')
        print(f'Q of diamonds')
    if num == 13:
        print(f'K of spades', end=', ')
        print(f'K of clubs', end=', ')
        print(f'K of hearts', end=', ')
        print(f'K of diamonds')
    if num == 14:
        print(f'A of spades', end=', ')
        print(f'A of clubs', end=', ')
        print(f'A of hearts', end=', ')
        print(f'A of diamonds')