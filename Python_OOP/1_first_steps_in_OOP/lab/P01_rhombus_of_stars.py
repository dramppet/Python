n = int(input())


def print_line(spaces_count, stars_counr):
    line_space = ''.join([' '] * space)
    line_stars = ' '.join(['*'] * stars)
    print(line_space + line_stars)


for i in range(n):
    space = n - i - 1
    stars = i + 1
    print_line(space, stars)

for i in range(n - 2, -1, -1):
    space = n - i - 1
    stars = i + 1
    print_line(space, stars)