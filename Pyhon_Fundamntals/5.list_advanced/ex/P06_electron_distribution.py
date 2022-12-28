# number_of_electrons = int(input())
# all_electrons = number_of_electrons
# electrons = []
# count_idx  = 0
# for idx in range(1,number_of_electrons):
#     curr_el = 2 * (idx **2)
#     if curr_el <= all_electrons:
#         electrons.append(curr_el)
#         all_electrons -= curr_el
#     if all_electrons == 0:
#         break
#
# if  all_electrons == 0:
#     print(electrons)
# else:
#     electrons.append(all_electrons)
#     print(electrons)

number_of_electrons = int(input())
electrons = []

shell_number = 1

while number_of_electrons > 0:
    max_electrons = 2 * shell_number**2
    if max_electrons > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(max_electrons)
    number_of_electrons -= max_electrons
    shell_number += 1

print(electrons)