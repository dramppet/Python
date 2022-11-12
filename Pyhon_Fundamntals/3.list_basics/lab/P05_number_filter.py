count = int(input())
even = list()
odd = list()
negative = list()
positive = list()

for _ in range(count):
    element = int(input())

    if element >= 0:
        positive.append(element)
    else:
        negative.append(element)

    if element %2 == 0:
        even.append(element)
    else:
        odd.append(element)

searched_list = input()

print(eval(searched_list))