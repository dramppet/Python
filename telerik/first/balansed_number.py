result = 0

while True:
    number = int(input())
    first = number // 100
    middle = (number // 10) % 10
    last = number % 10

    if middle != first + last:
        break
    result += number
print(result)