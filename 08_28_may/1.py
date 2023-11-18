favourite_book = input()
command = input()
book_count = 0

while command != "No More Books":

    if command == favourite_book:
        print(f"You checked {book_count} books and found it.")
        break
    book_count += 1
    command = input()
else:
    print(f"The book you search is not here!\n You checked {book_count} books.")