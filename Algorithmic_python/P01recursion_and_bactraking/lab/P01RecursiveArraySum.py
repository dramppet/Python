def sum_array(num, idx):
    if idx == len(num) - 1:
        return num[idx]
    return num[idx] + sum_array(num, idx + 1)

nums = [int(x) for x in input().split()]

print(sum_array(nums, 0))