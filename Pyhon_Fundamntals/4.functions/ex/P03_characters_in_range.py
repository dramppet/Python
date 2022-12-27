def characters_in_ranga(charA, charB):
    char_list = []
    for i in range(ord(charA) + 1, ord(charB)):
        char_list.append(chr(i))
    return char_list


first_char = input()
second_char = input()
print(' '.join(characters_in_ranga(first_char,second_char)))

