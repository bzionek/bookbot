import sys
from stats import count_words, count_chars, sort_chars

def main():
    #bookcontent = get_book_text("./books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print("Usage: python3 main.py <path_to_book>")
    #sys.exit(1)
    print(sys.argv)
    bookcontent = get_book_text(sys.argv[1])
    character_count = count_chars(bookcontent)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found", count_words(bookcontent), "total words")
    #print(character_count)
    print("--------- Character Count -------")
    sorted_chars = sort_chars(character_count)
    for sorted_char in sorted_chars:
        ch = sorted_char["char"]
        num = sorted_char["num"]
        if ch.isalpha() == True:
            print(f"{ch}: {num}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        bookcontent = f.read()
    return bookcontent

main()

