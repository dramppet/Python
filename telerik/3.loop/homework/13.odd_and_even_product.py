nums = [int(x) for x in input().split(' ')]

even = 1
odd = 1

for index in range(0,len(nums)):
    if index % 2 == 0:
        even *= nums[index]
    else:
        odd *= nums[index]

print('yes' if even == odd else 'no')