factor = int(input())
count = int(input())

list_of_numbers = []
for multiplier in range(1, count + 1):
    list_of_numbers.append(multiplier * factor)

print(list_of_numbers)