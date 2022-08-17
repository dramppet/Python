count_num = int(input())

words = {}

while count_num > 0:
    key = input()
    value = input()

    if key not in words:
        words[key] = []
        words[key].append(value)
    else:
        words[key].append(value)

    count_num -= 1

for key, value in words.items():
    print(f'{key} - {*value}')