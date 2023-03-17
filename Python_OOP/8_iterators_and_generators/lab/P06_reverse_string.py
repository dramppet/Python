def reverse_text(word):
    for char in reversed(word):
        yield char


for char in reverse_text("step"):
    print(char, end='')
