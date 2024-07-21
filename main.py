def read_book(book_path):
    with open(book_path) as raw_data:
        book_contents = raw_data.read()
    return book_contents


def main():
    print(read_book("books/frankenstein.txt"))

main()
