first_seq = input().split(', ')
second_seq = input().split(', ')

substrings = []

for first_word in first_seq:
    for items in second_seq:
        if first_word in items:
            substrings.append(first_word)
            break

print(substrings)