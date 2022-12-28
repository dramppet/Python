# world = input().split()
# filter_word = list(filter(lambda x: len(x) % 2 == 0,world))
# print('\n'.join(filter_word))

word = [x for x in input().split() if len(x) % 2 == 0]
print(*word,sep='\n')