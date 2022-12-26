def add_two_numbers(num1, num2):
    return num1 + num2


def subtract_three_number(rez, num):
    return rez - num


first_num = int(input())
second_num = int(input())
three_num = int(input())

add_tho = add_two_numbers(first_num,second_num)
rezult = subtract_three_number(add_tho, three_num)

print(rezult)
