number = int(input())

first = int(input())

result = str(first)

for _ in range(1,number):
    num = int(input())

    if first > num:
        result += '>'+ str(num)
        first = num
    elif first == num:
        result += '='+ str(num)
        first = num
    else:
        result +='<'+ str(num)
        first = num



print(result)