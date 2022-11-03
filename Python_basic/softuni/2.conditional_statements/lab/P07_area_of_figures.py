import math
type_figura = input()

area = 0.0

if type_figura == 'square':
    a = float(input())
    area = a * a
elif type_figura == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif type_figura == 'circle':
    r = float(input())
    area = math.pow(r,2) * math.pi
elif type_figura == 'triangle':
    a = float(input())
    h  = float(input())
    area = a * h /2

print(f"{area:.3f}")
