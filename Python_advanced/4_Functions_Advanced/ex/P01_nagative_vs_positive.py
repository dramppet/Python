numbers = list(map(int, input().split()))

# sum_positive = 0
# sum_negative = 0
#
# for num in numbers:
#     if num > 0:
#         sum_positive += num
#     else:
#         sum_negative += num

sum_positive = sum( el for el in numbers if el > 0)
sum_negative = sum( el for el in numbers if el < 0)

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')