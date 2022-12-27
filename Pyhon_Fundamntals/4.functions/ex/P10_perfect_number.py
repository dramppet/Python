def is_perfect(num):
    sum_digit = 0
    for curr_digit in range(1,num):
        if num % curr_digit == 0:
            sum_digit += curr_digit
    if sum_digit == num:
        return True
    return False


number = int(input())
if  is_perfect(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")