human_years = int(input())

dog_years = 0

if human_years <= 2:
    dog_years = human_years * 10
else:
    dog_years = (human_years - 2) * 4 + 20

print(dog_years)