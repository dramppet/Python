from collections import deque


def mark_words_letter(vowel, consonant, word_dict):
    result = False

    if vowel in word_dict:
        word_dict[vowel] = True
        result = True

    if consonant in word_dict:
        word_dict[consonant] = True
        result = True

    return result


rose = {letter: False for letter in "rose"}
tulip = {letter: False for letter in "tulip"}
lotus = {letter: False for letter in "lotus"}
daffodil = {letter: False for letter in "daffodil"}

vowels, consonants = deque(input().split()), deque(input().split())

flower_found = None
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    if mark_words_letter(vowel,consonant,rose):
        if all(rose.values()):
            flower_found = 'rose'
            break

    if mark_words_letter(vowel,consonant,tulip):
        if all(tulip.values()):
            flower_found = 'tulip'
            break

    if mark_words_letter(vowel,consonant,lotus):
        if all(lotus.values()):
            flower_found = 'lotus'
            break

    if mark_words_letter(vowel,consonant,daffodil):
        if all(daffodil.values()):
            flower_found = 'daffodil'
            break

if flower_found:
    print(f"Word found: {flower_found}")
else:
    print('Cannot find any word!')

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
