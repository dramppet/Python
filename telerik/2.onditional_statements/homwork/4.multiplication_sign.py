first = float(input())
second = float(input())
three = float(input())

countNegativeNumber = 0
countZeroNumber = 0
sign = ''

if first < 0:
    countNegativeNumber += 1
if second < 0:
    countNegativeNumber += 1
if three < 0:
    countNegativeNumber +=1

if first == 0:
    countZeroNumber +=1
if second == 0:
    countZeroNumber += 1
if three == 0:
    countZeroNumber +=1

if countNegativeNumber % 2 == 0 and countZeroNumber == 0:
    sign = '+'
elif countZeroNumber > 0:
    sign = '0'
else:
    sign = '-'


print(sign)