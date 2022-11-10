count_strings = int(int(input()))

for _ in range(count_strings):

    word = input()

    for i in range(len(word)):
        if word[i] == ',' or word[i] == '.' or word[i] == '_':
            print(f'{word} is not pure!')
            break
    else:
        print(f'{word} is pure.')


