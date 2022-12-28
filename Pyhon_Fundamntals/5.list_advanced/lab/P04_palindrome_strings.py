line_input = input().split(' ')
find_count_palindrome = input()

palindrome_list = []

for current_word in line_input:
    palindrome = current_word[::-1]

    if current_word == palindrome:
        palindrome_list.append(current_word)

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(find_count_palindrome)} times")