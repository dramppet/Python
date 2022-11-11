count = int(input())
searched_word = input()

words = []

for _ in range(count):
    word = input()
    words.append(word)

print(words)

for w in range(len(words)):
    current_word = words[w]

    if searched_word not in current_word:
        words.remove(current_word)
print(current_word)