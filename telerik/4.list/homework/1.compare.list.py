count_number_as_list = int(input())

first_list = []
second_list = []

def readList(numbers):
    input_list = []

    for _ in range(numbers):
        num = int(input())
        input_list.append(num)

    return input_list


first_list = readList(count_number_as_list)
second_list = readList(count_number_as_list)
is_qual = True

for num in range(len(first_list)):
    if first_list[num] != second_list[num]:
        is_qual = False
        break

if is_qual:
    print('Equal')
else:
    print('Not equal')
