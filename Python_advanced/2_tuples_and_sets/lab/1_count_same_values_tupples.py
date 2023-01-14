numbers = tuple(map(lambda x: float(x), input().split()))
num = []

for n in numbers:
   if n not in num:
        num.append(n)
        print(f"{n} - {numbers.count(n)} times")
   else:
       continue