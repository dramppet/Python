n = int(input())

for num in range(1,n + 1):
    number_as_string = str(num)
    digit = 0
    for nums in number_as_string:
        digit+=int(nums)
    if digit == 5 or digit == 7 or digit == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')