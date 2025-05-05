
import sys
from stats import (
    num_words, 
    character_amount, 
    sort_character_counts
)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_of_file = sys.argv[1]
    book_content = get_book_text(path_of_file)
    count = num_words(book_content)
    char = character_amount(book_content)
    sorted_chars = sort_character_counts(char)
    print_report(path_of_file, count, sorted_chars)
    
    
    
def print_report(path_of_file, count, sorted_chars):
    
    print("=========BOOKBOT==========")
    print(f"Analyzing book found at {path_of_file}...")
    print("---------Word Count---------")
    print(f"Found {count} total words")
    print("---------Character Count--------")
    
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

           
    print("==========End==========")

    
main()
