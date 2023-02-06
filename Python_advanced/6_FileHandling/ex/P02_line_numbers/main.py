from string import punctuation

with open("text.txt","r") as fail:
    text_file = fail.readlines()

output_file = open("output.txt", "w")

for line in range(len(text_file)):
    line_text = text_file[line]

    letters = 0
    marks = 0

    for symbols in line_text:
        if symbols.isalpha():
            letters +=1
        elif symbols in punctuation:
            marks += 1
    output_file.write(f"Line {line+ 1}: {line_text} ({letters})({marks})\n")

output_file.close()