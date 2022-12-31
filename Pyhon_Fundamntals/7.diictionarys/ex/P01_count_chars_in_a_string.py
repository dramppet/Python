line = input()
count_chars = {}

for symbols in line:
    if symbols not in count_chars:
        count_chars[symbols] = 0
    count_chars[symbols] += 1

for key, value in count_chars.items():
    if key != " ":
        print(f"{key} -> {value}")