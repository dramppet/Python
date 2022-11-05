budget = float(input())
season = input()

destination = ''
trip = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        trip = 'Camp'
        budget *= 0.3
    else:
        trip = 'Hotel'
        budget *= 0.7
elif budget > 1000:
    trip = 'Hotel'
    destination = 'Europe'
    budget *= 0.9
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        trip = 'Camp'
        budget *= 0.4
    else:
        trip = 'Hotel'
        budget *= 0.8

print(f'Somewhere in {destination}')
print(f'{trip} - {budget:.2f}')

