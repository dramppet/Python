nums = []

nums.append(5)
nums.append(6)
nums.insert(0,4)

print(nums)
print(nums[1])

nums.pop()

for num in nums:
    print(num,end=', ')
