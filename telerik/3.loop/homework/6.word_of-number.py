text_input = input()

for num in text_input:
    if num >= '0' and num <= '9' or num == '-':
        print(float(text_input) + 1)
        break
    else:
        print(text_input[::-1])
        break

