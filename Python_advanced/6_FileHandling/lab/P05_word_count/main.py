file_name = open('word.txt','r')
searched_file = open('input.txt', 'r')


dict_searched = {}

for line in file_name.read().split(" "):
    if line in searched_file.read().split(" "):
        dict_searched[line]  = 0
    dict_searched[line] += 1