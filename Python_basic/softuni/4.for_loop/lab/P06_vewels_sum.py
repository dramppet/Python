word = input()

sum_char = 0

for char in word:
    if char == 'a':
        sum_char += 1
    elif char == 'e':
        sum_char += 2
    elif char == 'i':
        sum_char += 3
    elif char == 'o':
        sum_char += 4
    elif char == 'u':
        sum_char += 5

print(sum_char)