from collections import deque

milligrams_of_caffeine, energy_drinks = deque(list(map(int,input().split(", ")))), deque(list(map(int,input().split(", "))))

MAM_CAFFEINE = 300
Stamat_caffeine = 0
while True:
    if len(milligrams_of_caffeine) == 0:
        break
    if len(energy_drinks) == 0:
        break
    milligram = milligrams_of_caffeine.pop()
    drink = energy_drinks.popleft()

    caffein = milligram * drink

    if Stamat_caffeine + caffein< MAM_CAFFEINE:
        Stamat_caffeine += caffein
    else:
        energy_drinks.append(drink)
        Stamat_caffeine -= 30
        if Stamat_caffeine < 0:
            Stamat_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {Stamat_caffeine} mg caffeine.")