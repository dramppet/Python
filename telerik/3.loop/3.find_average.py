number_count = int(input())

sum_numbers = 0.0

for _ in range(number_count):
    num = float(input())
    sum_numbers += num

avg = sum_numbers / number_count

print(f'{avg:.2f}')
    