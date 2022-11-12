count = int(input())
searched_word = input()
strings = list()
fil_strings = list()

for _ in range(count):
    current_strings = input()
    strings.append(current_strings)
    if searched_word in current_strings:
        fil_strings.append(current_strings)

print(strings)
print(fil_strings)