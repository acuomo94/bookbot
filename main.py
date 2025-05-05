from stats import num_words, character_amount, sort_character_counts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

    
def main():
    book_content = get_book_text("/home/acuomo/workspace/github.com/acuomo/bookbot/books/frankenstein.txt")
    count = num_words(book_content)
    char = character_amount(book_content)
    sorted_chars = sort_character_counts(char)
    print("=========BOOKBOT==========")
    print("Analyzing book found at books/frankenstein.txt...")
    print("---------Word Count---------")
    print(f"Found {count} total words")
    print("---------Character Count--------")
    
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("==========End==========")

    
main()
