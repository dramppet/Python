def sum_even_and_odd(num_str):
    even_sum = 0
    odd_sum = 0

    for num in range(len(num_str)):
        nums = int(num_str[num])
        if nums % 2 == 0:
            even_sum += nums
        else:
            odd_sum += nums

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


number_string = input()
print(sum_even_and_odd(number_string))