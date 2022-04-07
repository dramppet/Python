book_name = input()

curr_book = input()
counter = 0
book_is_found = False
while not curr_book == 'No More Books':

    if curr_book == book_name:
        book_is_found = True
        break

    counter += 1
    curr_book = input()

if book_is_found:
    print(f'You checked {counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')