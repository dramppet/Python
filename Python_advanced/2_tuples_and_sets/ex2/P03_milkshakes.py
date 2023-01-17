from collections import deque

chocolates = list(map(int,input().split(', ')))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:

    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    if chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    if cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
        continue
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)


print("Great! You made all the chocolate milkshakes needed!" if milkshakes >= 5 else f"Not enough milkshakes.")
if len(chocolates) > 0:
    print(f"Chocolate: {', '.join(map(str,chocolates))}")
else:
    print("Chocolate: empty")

if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join(map(str,cups_of_milk))}")
else:
    print("Milk: empty")

