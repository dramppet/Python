product = input()
city = input()
quantity = float(input())
price = 0

if  product == "coffee":
    if city == "Sofia":
        price = 0.5
    elif city == "Plovdiv":
        price = 0.4
    elif city == "Varna":
        price = 0.45
elif product == "water":
    if city == "Sofia":
        price = 0.8
    elif city == "Plovdiv":
        price = 0.7
    elif city == "Varna":
        price = 0.7
elif product == "beer":
    if city == "Sofia":
        price = 1.2
    elif city == "Plovdiv":
        price = 1.15
    elif city == "Varna":
        price = 1.1
elif product == "sweets":
    if city == "Sofia":
        price = 1.45
    elif city == "Plovdiv":
        price = 1.3
    elif city == "Varna":
        price = 1.35
elif product == "peanuts":
    if city == "Sofia":
        price = 1.6
    elif city == "Plovdiv":
        price = 1.5
    elif city == "Varna":
        price = 1.55

print(quantity * price)
