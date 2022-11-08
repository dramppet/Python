searched_book = input()

searched_books_count = 0
is_find = False

while True:
    book = input()

    if book == 'No More Books':
        print("The book you search is not here!")
        print(f'You checked {searched_books_count} books.')
        break

    if book == searched_book:
        print(f'You checked {searched_books_count} books and found it.')
        break

    searched_books_count += 1

