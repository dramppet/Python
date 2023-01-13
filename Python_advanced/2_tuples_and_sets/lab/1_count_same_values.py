line = [float(x) for x in input().split()]
counts = {}

for el in line:
    if el not in counts:
        counts[el] = 1
    else:
        counts[el] += 1

for key,value in counts.items():
    print(f"{key} - {value} times")