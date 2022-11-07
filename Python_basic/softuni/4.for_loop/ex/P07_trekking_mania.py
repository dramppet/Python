count_group = int(input())

group_Musalla = 0
group_Momblan = 0
group_Kilimandgaro = 0
group_K2 = 0
group_Eurest = 0
all_group = 0


for _ in range(count_group):
    group = int(input())
    all_group += group

    if group <= 5:
        group_Musalla += group
    elif 6 <= group <= 12:
        group_Momblan += group
    elif 13 < group <= 25:
        group_Kilimandgaro += group
    elif 26 <= group <= 40:
        group_K2 += group
    elif group >= 41:
        group_Eurest += group

print(f'{((group_Musalla / all_group)*100):.2f}%')
print(f'{((group_Momblan / all_group)*100):.2f}%')
print(f'{((group_Kilimandgaro / all_group)*100):.2f}%')
print(f'{((group_K2 / all_group)*100):.2f}%')
print(f'{((group_Eurest / all_group)*100):.2f}%')

