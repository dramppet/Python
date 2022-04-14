def number_name (number):
    if number == 0:
        print('Zero')
    elif number == 1:
        print('One')
    elif number == 2:
        print('Two')
    elif number == 3:
        print('Three')
    elif number == 4:
        print('Four')
    elif number == 5:
        print('Five')
    elif number == 6:
        print('Six')
    elif number == 7:
        print('Seven')
    elif number == 8:
        print('Eight')
    elif number == 9:
        print('Nine')

def number_teen(number):
    if number == 10:
        print('Ten')
    elif number == 11:
        print('Eleven')
    elif number == 12:
        print('Twelve')
    elif number == 13:
        print('Thirteen')
    elif number == 14:
        print('Fourteen')
    elif number == 15:
        print('Fifteen')
    elif number == 16:
        print('Sixteen')
    elif number == 17:
        print('Seventeen')
    elif number == 18:
        print('Eighteen')
    elif number == 19:
        print('Nineteen')

def number_decimals(number):
    if number == 2:
        print('Twenty')
    elif number == 3:
        print('Thirty')
    elif number == 4:
        print('Fourty')
    elif number == 5:
        print('Fivty')
    elif number == 6:
        print('Sixty')
    elif number == 7:
        print('Seventy')
    elif number == 8:
        print('Eighty')
    elif number == 9:
        print('Ninety')

num = int(input())

thousands = num  / 1000
hundreds = (num % 1000) / 100
decimal = (num % 100) / 10
single = num % 10

if(thousands):
    print(f'{number_name(thousands)} thousand')

if(hundreds):
    print(f'{number_name(thousands)} hundred')

if decimal >= 2:
    print(number_decimals(decimal))
    if single:
        print(number_name(single))
else:
    if decimal == 1:
        print(number_teen(num % 100))
    else:
        if num == 0 or single !=0:
            print(number_name(single))







