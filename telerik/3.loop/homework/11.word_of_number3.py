count_input = int(input())

sum_numbers = 0
str_input = ''

while True:

    if count_input == 0:
        break

    text_input = input()

    if text_input[0] >= '0' and text_input[0] <='9' or text_input[0] == '-':
        sum_numbers += int(text_input)
        if len(str_input) > 0:
            print(str_input.strip('-'))
            str_input = ''

    else:
        str_input += text_input
        str_input += '-'
        if sum_numbers > 0:
            print(sum_numbers)
            sum_numbers = 0



    count_input -= 1

if len(str_input) > 0:
    print(str_input.strip('-'))

if sum_numbers > 0:
    print(sum_numbers)
