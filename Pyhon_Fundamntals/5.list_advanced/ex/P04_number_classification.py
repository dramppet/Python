numbers_input = [int(x) for x in input().split(", ")]
positive = list(filter(lambda num: num>= 0,numbers_input))
negative = list(filter(lambda num: num < 0,numbers_input))
even = list(filter(lambda num: num % 2 == 0,numbers_input))
odd = list(filter(lambda num: num % 2 != 0,numbers_input))

print(f"Positive: {', '.join([str(el) for el in positive])}")
print(f"Negative: {', '.join([str(el) for el in negative])}")
print(f"Even: {', '.join([str(el) for el in even])}")
print(f"Odd: {', '.join([str(el) for el in odd])}")
