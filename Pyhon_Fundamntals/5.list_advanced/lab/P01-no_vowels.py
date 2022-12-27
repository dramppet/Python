
vowels = ['a', 'o', 'u', 'e', 'i']

word2 = [char for char in input() if char.lower() not in vowels]

print(''.join(word2))

