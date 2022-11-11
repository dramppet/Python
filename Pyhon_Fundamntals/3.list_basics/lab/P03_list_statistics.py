n = int(input())

positive = []
negative = []
sum_negatives = 0

for _ in range(n):
    num = int(input())

    if num < 0:
        negative.append(num)
        sum_negatives += num
    else:
        positive.append(num)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum_negatives}')