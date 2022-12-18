list_of_numbers = input().split()

opposite_number = []

for element in list_of_numbers:
    current_number = -int(element)
    opposite_number.append(current_number)

print(opposite_number)