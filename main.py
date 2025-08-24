import sys
from stats import (
    get_num_words, 
    get_chars_dict, 
    get_sorted_chars_dict,
    )


def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        print(f"Found {num_words} total words")
        sorted_chars = get_sorted_chars_dict(chars_dict)
        for item in sorted_chars: 
            if item["char"].isalpha():  
                print(f"{item['char']}: {item['num']}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()