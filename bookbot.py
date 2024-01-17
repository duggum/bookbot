"""bookbot

A Python program that can analyze an entire book's text and print out an
interesting statistical report.
"""

from collections import Counter


def main() -> None:
    book: str = "books/frankenstein.txt"

    # get the text from book
    text: str = get_text(book)

    # get the word count
    words: int = get_words(text)

    # get the character counts and sort them
    chars: Counter = get_char_counts(text)

    # print report
    print("\n----------------- BookBot Statistical Analysis -----------------\n")
    print(f"Book:\n\n\t{book.removeprefix("books/")}\n")
    print(f"Word Count:\n\n\t{words}\n")
    print("Letter Counts:\n")

    # iterate over the sorted chars dict
    for key, val in sorted(chars.items()):

        # only print letter counts
        if key.isalpha():
            print(f"\t'{key}' = {val}")
    print("\n----------------------------------------------------------------\n")


def get_char_counts(text: str) -> Counter:
    """Get the number of occurences of each unique character in a string

    Args:
        text (str): the text to parse

    Returns:
        Counter: a Counter containing all of the character counts
    """
    lower_text: str = text.lower()
    return Counter(lower_text)


def get_words(text: str) -> int:
    """Get the number of words in a string

    Args:
        text (str): the text to parse

    Returns:
        int: the number of words in the text
    """
    return len(text.split())


def get_text(path: str) -> str:
    """get the text from a text file

    Args:
        path (str): the path of the file to read

    Returns:
        str: the file text
    """
    with open(path) as file:
        return file.read()


if __name__ == "__main__":
    main()
