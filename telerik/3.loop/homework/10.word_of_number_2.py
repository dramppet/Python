count_input = int(input())

numbers = '0123456789'

sum = 0
str_input = ''

while True:
    if count_input == 0:
        break

    text = input()

    if text in numbers:
        sum += int(text)
    else:
        str_input += text
        str_input += '-'

    count_input -= 1

print_str = str_input.strip('-') if len(str_input) > 0  else'no words'
print(print_str)
print(sum)