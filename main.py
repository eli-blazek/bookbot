def read_book(book_path):
    with open(book_path) as raw_data:
        book_contents = raw_data.read()
    return book_contents

def count_words():
    data_source = read_book("books/frankenstein.txt")
    words = data_source.split()
    return len(words)

def count_chars():
    pass

def main():
    print(count_words())


main()