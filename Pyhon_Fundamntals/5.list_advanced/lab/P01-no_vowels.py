word = input()

vowels = ['a', 'o', 'u', 'e', 'i']

words = list()

for char in  word:
    if char in vowels:
        continue
    else:
        words.append(char)

print(''.join(words))