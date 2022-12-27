def fact(number):
    num = 1
    for curr_num in range(1,number +1):
        num *= curr_num
    return num

num_one = int(input())
num_two = int(input())

fact_one = fact(num_one)
fact_two = fact(num_two)

print(f'{(fact_one / fact_two):.2f}')
