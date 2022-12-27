def is_palindrome(number: str):
    bool_palindrome = []
    for n in number:
        num = n
        palindrome = num[::-1]

        if num == palindrome:
            bool_palindrome.append('True')
        else:
            bool_palindrome.append('False')

    return bool_palindrome


number_str = input().split(', ')
print('\n'.join(is_palindrome(number_str)))
