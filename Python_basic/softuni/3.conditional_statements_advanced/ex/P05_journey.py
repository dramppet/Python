budget = float(input())
season = input()

destination = ''
place = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        budget *= 0.3
    else:
        place = 'Hotel'
        budget *= 0.7
elif budget > 1000:
    place = 'Hotel'
    destination = 'Europe'
    budget *= 0.9
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        budget *= 0.4
    else:
        place = 'Hotel'
        budget *= 0.8

print(f'Somewhere in {destination}')
print(f'{place} - {budget:.2f}')

