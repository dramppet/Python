count_char = int(input())

sum_char = 0

for _ in range(count_char):
    char_single = input()
    sum_char += ord(char_single)

print(f'The sum equals: {sum_char}')