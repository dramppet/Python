name_actor = input()
point_academia = int(input())
count_price = int(input())

length_actor = len(name_actor)
is_break = False
point_actor = 0

for _ in range(count_price):
    name_price = input()
    point_price = float(input())
    point = point_academia + ((len(name_price) * point_price) / 2)
    point_academia = point

    if point > point_actor:
        point_actor = point

    if point > 1250.5:
        is_break = True
        break

if is_break:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {point_actor}!')
else:
    print(f'Sorry, {name_actor} you need {1250.5 - point_actor:.1f} more!')


