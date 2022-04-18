max_length = 0
word = ''

while True:
    text = input()

    if text == 'END':
        break

    if max_length <= len(text):
        max_length = len(text)
        word = text

print(word)