def read_book(book_path):
    with open(book_path) as raw_data:
        book_contents = raw_data.read()
    return book_contents

def count_words(text_source):
    words = text_source.split()
    return len(words)

def count_chars(text_source):
    pass

def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    count_chars(text)
    print(count_words(text))

main()