def linear_serched(target, nums):
    for index,num in enumerate(nums):
        if target == num:
            return index
    return False
nums = [1, 2, 3, 8, 9, 11]
target =11

print(linear_serched(target, nums))

