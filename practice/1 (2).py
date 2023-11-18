favourite_book = input()
book_count = 0
is_book_found = False
book_name = input()

while book_name != "No More Books":
    if book_name == favourite_book:
        print(f"You checked {book_count} books and found it.")
        is_book_found = True
        break
    book_count += 1
    book_name = input()
if book_name == "No More Books":
    print(f"The book you search is not here!\n"
              f"You checked {book_count} books.")




