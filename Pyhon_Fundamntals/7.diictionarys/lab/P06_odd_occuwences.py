data = input().split()
words = {}

for word in data:
    word_lower = word.lower()

    if word_lower not in words:
        words[word_lower] = 0
    words[word_lower] += 1

for key, value in words.items():
    if value % 2 != 0:
        print(key, end=' ')
