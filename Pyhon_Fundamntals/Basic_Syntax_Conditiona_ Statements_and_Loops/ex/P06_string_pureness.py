count_strings = int(int(input()))

for _ in range(count_strings):

    word = input()

    for char in word:
        if char == ',' or char == '.' or char == '-':
            print(f'{word} is not pure!')
            break
    print(f'{word} is pure.')