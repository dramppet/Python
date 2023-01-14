count_line = int(input())

periodic_set = set()

for _ in range(count_line):
    command = input().split()
    for i in command:
        periodic_set.add(i)

print('\n'.join(periodic_set))
