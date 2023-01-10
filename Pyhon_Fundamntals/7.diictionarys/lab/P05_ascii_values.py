line_ascii_symbols = input().split(", ")
ascii_values = {}

for synbols in line_ascii_symbols:
    key = synbols
    value = ord(synbols)
    ascii_values[key] = value

print(ascii_values)


# print({key:ord(key) for key in input().split(", ")})
