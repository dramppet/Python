labels = input()
ranks = int(input())

colors = ''

if labels == 'a' or labels == 'c' or labels =='e' or labels == 'g':
    if ranks % 2 == 0:
        colors = 'light'
    else:
        colors = 'dark'
else:
    if ranks % 2 == 0:
        colors = 'dark'
    else:
        colors = 'light'

print(colors)