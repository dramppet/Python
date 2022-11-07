count_group = int(input())

group_Musala = 0
group_Monblan = 0
group_Kilimanjaro = 0
group_K2 = 0
group_Everest = 0
all_group = 0

for _ in range(count_group):
    group = int(input())
    all_group += group

    if group < 6:
        group_Musala += group
    elif group < 13:
        group_Monblan += group
    elif group < 26:
        group_Kilimanjaro += group
    elif group < 41:
        group_K2 += group
    else:
        group_Everest += group

print(f'{((group_Musala / all_group) * 100):.2f}%')
print(f'{((group_Monblan / all_group) * 100):.2f}%')
print(f'{((group_Kilimanjaro / all_group) * 100):.2f}%')
print(f'{((group_K2 / all_group)*100):.2f}%')
print(f'{((group_Everest / all_group) * 100):.2f}%')

