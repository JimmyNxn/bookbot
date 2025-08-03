import os


def count_chars(text):
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            if char == " ":
                continue
            char_count_dict[char] = 1
    sorted_char_count_dict = sorted(
        char_count_dict.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_char_count_dict


def get_book_text(book):
    # Fetch book text from .txt file
    with open(os.path.join(book), "r") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def print_report(sorted_char_count_dict, word_count, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}... ")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_char_count_dict:
        print(f"{char}: {count}")
