def get_open_book(path):
    with open(path) as f:
        open_book = f.read()
    return open_book

def get_count_words(res_string):
    words = res_string.split()
    print(len(words))

def main():
    book = get_open_book("books/frankenstein.txt")
    get_count_words(book)

main()



