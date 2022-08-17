count_num = int(input())

words = {}

while count_num > 0:
    key = input()
    value = input()

    if key not in words:
        words[key] = []
    words[key].append(value)

    count_num -= 1

for keys, values in words.items():
    print(f"{keys} - {', '.join(values)}")
