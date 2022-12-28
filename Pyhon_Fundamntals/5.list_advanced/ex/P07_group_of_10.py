number = [int(num) for num in input().split(", ")]

# numbers = list(map(lambda  x: int(x), input().split(", ")))

group = 10
max_number = max(number)

while number:
    nums_group = []

    for num in number:
        if num in range(group - 10, group + 1):
            nums_group.append(num)

    for num in nums_group:
        number.remove(num)
    print(f"Group of {group}'s: {nums_group}")
    group += 10