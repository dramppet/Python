graph = {}

while True:
    line = input()

    if line == 'End':
        break

    node, children_str = [x.strip() for x in line.split('->')]
