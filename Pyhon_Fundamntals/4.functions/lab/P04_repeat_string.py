# def repeat_string(input_str,count):
#     return input_str * count
#
word_repeat = input()
count_repeat = int(input())
#
# print(repeat_string(word_repeat,count_repeat))

rep_str = lambda a, b: a * b
result = (rep_str(word_repeat, count_repeat))
print(result)
