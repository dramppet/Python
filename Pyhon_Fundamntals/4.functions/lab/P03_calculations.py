def calculation(num_a, num_b, oper):
    if oper == 'multiply':
        return num_a * num_b
    elif oper == 'divide':
        return int(num_a / num_b)
    elif oper == 'add':
        return num_a + num_b
    elif oper == 'subtract':
        return num_a - num_b


operation = input()
num_first = int(input())
num_second = int(input())

print(calculation(num_first,num_second,operation))
