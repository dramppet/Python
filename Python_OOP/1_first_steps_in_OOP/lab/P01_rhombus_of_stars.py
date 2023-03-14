size = int(input())


def print_line(spaces_count, stars_counr):
    line_space = ''.join([' '] * space)
    line_stars = ' '.join(['*'] * stars)
    print(line_space + line_stars)


for i in range(size):
    space = size - i - 1
    stars = i + 1
    print_line(space, stars)

for i in range(size- 2, -1, -1):
    space = size - i - 1
    stars = i + 1
    print_line(space, stars)