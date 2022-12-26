money_list = input().split(", ")
number_of_beggars = int(input())

final_sums = []
money_list_as_digit = []
starting_index = 0

for element in money_list:
    money_list_as_digit.append(int(element))
