from collections import deque

rows, columns = list(map(int,input().split()))
word = list(input())

word_copy = deque(word)

for r in range(rows):
    while len(word_copy) < columns:
        word_copy.extend(word)

    if r % 2 == 0:
        print(*[word_copy.popleft() for _ in range(columns)],sep='')
    else:
        print(*[word_copy.popleft() for _ in range(columns)][::-1],sep='')