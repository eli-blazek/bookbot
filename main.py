def read_book(book_path):
    with open(book_path) as raw_data:
        book_contents = raw_data.read()
    return book_contents

def count_words(text_source):
    words = text_source.split()
    return len(words)

def count_chars(text_source):
    lower_book = text_source.lower()
    my_chars = {}
    for char in lower_book:
        if char.isalpha():
            if char in my_chars:
                my_chars[char] += 1
            else:
                my_chars[char] = 1

    return my_chars
def sort_func(input_dict):
    return input_dict["count"]

def counting_chars(dict_of_chars):
    list_of_chars = []
    for char in dict_of_chars:
        list_of_chars.append(
            {
                "name": char,
                "count": dict_of_chars[char]
            }
        )
    list_of_chars.sort(key=sort_func, reverse = True)
    return list_of_chars

def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    count_chars(text)
    words = count_words(text)
    chars = count_chars(text)
    lst_of_dicts = counting_chars(chars)
    print(f"This is a book report of book {path}")
    print(f"Number of words in this book is {words}")
    for dict in lst_of_dicts:
        print(f"Character {dict['name']} appears {dict['count']} times")

main()