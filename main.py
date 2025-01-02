def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)
    print(characters)

def count_characters(text):
    lower_string = text.lower()
    letters_dict = {}
    for c in lower_string:
        if c in letters_dict:
            letters_dict[c] += 1
        else:
            letters_dict[c] = 1
    return letters_dict


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()