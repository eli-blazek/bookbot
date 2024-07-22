def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    print(count_words(text))

def read_book(book_path):
    with open(book_path) as raw_data:
        book_contents = raw_data.read()
    return book_contents

def count_words(text_source):
    words = text_source.split()
    return len(words)

def count_chars():
    pass

main()