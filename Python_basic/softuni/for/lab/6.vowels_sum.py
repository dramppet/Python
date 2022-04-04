words = input()

sum_vowel = 0

for i in words:
    if i == 'a':
        sum_vowel += 1
    elif i == 'e':
        sum_vowel += 2
    elif i == 'i':
        sum_vowel += 3
    elif i == 'o':
        sum_vowel += 4
    elif i == 'u':
        sum_vowel += 5

print(sum_vowel)