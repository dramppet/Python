from math import sqrt,pow

a = float(input())
b = float(input())
c = float(input())

discriminant = pow(b,2) - 4 * a * c

x1 = (- b - sqrt(discriminant)) / (2 * a)
x2 = (- b + sqrt(discriminant)) / (2 * a)

print(f'x1 ={x1:g}; x2 ={x2:g}')