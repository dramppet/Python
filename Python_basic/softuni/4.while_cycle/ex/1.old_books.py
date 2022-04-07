book_name = input()

curr_book = input()
counter = 0
while not curr_book == book_name:

    if curr_book == 'No More Books':
        break

    counter += 1
    curr_book = input()

if curr_book == book_name:
    print(f'You checked {counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')