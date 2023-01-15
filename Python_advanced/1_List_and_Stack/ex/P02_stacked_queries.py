map_functions = {
    1: lambda x:stacks.append(x[1]),
    2: lambda x: stacks.pop() if len(stacks) > 0 else None,
    3: lambda x: print(max(stacks)) if len(stacks) > 0 else None,
    4: lambda x:print(min(stacks)) if len(stacks) > 0 else None,
}

count_rows = int(input())
stacks = []

for _ in range(count_rows):
    number_data = [int(x) for x in input().split()]
    map_functions[number_data[0]](number_data)
stacks.reverse()
print(*stacks,sep=', ')