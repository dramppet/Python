num_count = int(input())

nums = []

for _ in range(num_count):
    num = int(input())
    nums.append(num)

print(max(nums))