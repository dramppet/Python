text_input = input()

number_find = '0123456789'

for num in text_input:
    if num in number_find:
        print(float(text_input) + 1)
        break
    else:
        print(text_input[::-1])
        break