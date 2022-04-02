w = float(input())
h = float(input())

koridor = h * 100 -100

bura = koridor // 70
red = (w * 100) // 120

all = (bura * red) - 3

print(round(all))


