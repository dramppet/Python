from math import pi,pow

figures = input()

result = 0.0
if figures == 'square':
    a = float(input())
    result = pow(a,2)
elif figures == 'rectangle':
    a = float(input())
    h = float(input())
    result = a * h
elif figures == 'circle':
    a = float(input())
    result = pi * pow(a,2)
else:
    a = float(input())
    h = float(input())
    result = (a * h) / 2

# print(f'{result:.3f}')
print(round(result,3))
