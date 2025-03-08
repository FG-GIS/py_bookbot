from stats import count_words,count_char_instances,format_dict
import sys

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def fmt_output(wordcount: int,path: str,elab: dict):
    msg = (f"============ BOOKBOT ============\n"
            f"Analyzing book found at {path}\n"
            f"----------- Word Count ----------\n"
            f"Found {wordcount} total words\n"
            f"--------- Character Count -------\n")
    for e in elab:
        if e["char"].isalpha():
            msg += f"{e['char']}: {e['value']}\n"
    msg += f"============= END ===============\n"
    return msg


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    w_count = count_words(book_text)
    # print(f"{w_count} words found in the document")
    char_dict = count_char_instances(book_text)
    # print(char_dict)
    # print(format_dict(char_dict))
    print(fmt_output(w_count,book_path,format_dict(char_dict)))

main()