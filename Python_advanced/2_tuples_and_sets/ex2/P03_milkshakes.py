from collections import deque

chocolates = list(map(int,input().split(', ')))
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while True:

    if len(chocolates)  == 0:
        break
    if len(cups_of_milk) == 0:
        break

    if milkshakes == 5:
        break

    choko = chocolates.pop()
    milk = cups_of_milk.popleft()

    if choko <= 0:
        cups_of_milk.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(choko)
        continue

    if choko == milk:
        milkshakes += 1
        continue
    else:
        cups_of_milk.append(milk)
        chocolates.append(choko - 5)


print("Great! You made all the chocolate milkshakes needed!" if milkshakes >= 5 else f"Not enough milkshakes.")
if len(chocolates) > 0:
    print(f"Chocolate: {', '.join(map(str,chocolates))}")
else:
    print("Chocolate: empty")

if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join(map(str,cups_of_milk))}")
else:
    print("Milk: empty")

