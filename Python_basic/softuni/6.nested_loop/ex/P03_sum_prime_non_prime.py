sum_of_prime_numbers, sum_non_prime_numbers = 0, 0

while True:
    command = input()

    if command == 'stop':
        break

    current_number = int(command)
    is_prime = True

    if current_number < 0:
        print('Number is negative.')
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_of_prime_numbers += current_number
    else:
        sum_non_prime_numbers += current_number

print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')


