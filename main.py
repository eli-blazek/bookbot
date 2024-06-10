def main(book):
    with open(book) as f:
        open_book = f.read()
        words = open_book.split()
        print(len(words))

main("books/frankenstein.txt")