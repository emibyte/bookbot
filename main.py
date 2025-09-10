from stats import count_words, count_characters, sort_list_of_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_list(sorted_count):
    for item in sorted_count:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
            
def get_report(word_count, char_count, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_count = sort_list_of_characters(char_count)
    print_list(sorted_count)
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        contents = get_book_text(book)
        word_count = count_words(contents)
        char_count = count_characters(contents)
        get_report(word_count, char_count, book)

main()
