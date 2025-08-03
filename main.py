from stats import count_chars, get_book_text, count_words, print_report
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = count_words(text)
    num_chars = count_chars(text)

    print_report(num_chars, num_words, book)
    sys.exit(0)
