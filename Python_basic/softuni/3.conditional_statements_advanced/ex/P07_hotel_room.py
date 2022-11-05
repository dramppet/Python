month = input()
count_overnight = int(input())

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    price_studio = count_overnight * studio
    price_apartment = count_overnight * apartment
    if count_overnight > 14:
        price_studio *= 0.7
        price_apartment *= 0.9
    elif count_overnight > 7:
        price_studio *= 0.95
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7
    price_studio = count_overnight * studio
    price_apartment = count_overnight * apartment
    if count_overnight > 14:
        price_studio *= 0.8
        price_apartment *= 0.9
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    price_studio = count_overnight * studio
    price_apartment = count_overnight * apartment
    if count_overnight > 14:
        price_apartment *= 0.9
    print(f'Apartment: {price_apartment:.2f} lv.')
    print(f'Studio: {price_studio:.2f} lv.')