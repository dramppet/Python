from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue","orange", "purple", "green"}
red_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + words):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[::-1], second_word[::-1]):
            if el:
                words.insert(len(words) // 2 ,el)