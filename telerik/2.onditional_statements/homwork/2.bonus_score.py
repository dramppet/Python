point = int(input())

bonus = 0
is_bonus = True

if point > 0 and point < 4:
    bonus = point * 10
elif point > 3 and point < 7:
    bonus = point * 100
elif point > 6 and point < 10:
    bonus = point * 1000
else:
    is_bonus = False
    print('Invalid score')

if is_bonus:
    print(bonus)