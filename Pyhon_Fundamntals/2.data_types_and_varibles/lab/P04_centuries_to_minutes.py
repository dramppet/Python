import math

cantries = int(input())
years = cantries * 100
days = math.trunc(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{cantries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')