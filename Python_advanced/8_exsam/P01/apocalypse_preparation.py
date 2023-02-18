from collections import deque

textiles = deque(list(map(int,input().split(" "))))
medicaments = deque(list(map(int,input().split(" "))))

healing_item = {
    30: "Patch",
    40:"Bandage",
    100: "MedKit",
}

elements = {}

while medicaments:

    if len(textiles) <= 0:
        break

    textile = textiles.popleft()
    medicament = medicaments.pop()

    product = textile + medicament

    if product in healing_item:
        item = healing_item[product]
        if item not in elements:
            elements[item]  = 1
        else:
            elements[item] += 1
    elif product > 100:
        if 'MedKit' not in elements:
            elements['MedKit'] = 1
        else:
            elements['MedKit'] += 1
        if len(medicaments) > 0:
            medicaments[-1] = medicaments[-1] + (product - 100)
    else:
        medicaments.append(medicament + 10)

if len(medicaments) == 0 and len(textiles) == 0:
    print("Textiles and medicaments are both empty.")
elif  len(medicaments) == 0:
    print('Medicaments are empty.')
elif len(textiles) == 0:
    print('Textiles are empty.')

if elements:

    sorted_d = sorted(elements.items(),key = lambda x: (-x[1],x[0]))

    for el, it in sorted_d:
        print(f"{el} - {it}")

if len(medicaments) > 0:
    med = reversed(medicaments)
    print(f"Medicaments left: {', '.join([str(x) for x in med])}")
if len(textiles) > 0:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")