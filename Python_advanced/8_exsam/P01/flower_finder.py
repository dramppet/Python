from collections import deque

rose = {letter:False for letter in "rose"}
tulip = {letter:False for letter in "tulip"}
lotus = {letter:False for letter in "lotus"}
daffodil = {letter:False for letter in "daffodil"}

vowels, consonants = deque(input().split()), deque(input().split())

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()