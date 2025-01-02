def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)
    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document")
    new_dict = sort_dict(characters)
    for key, value in new_dict.items():
        print (f"The '{key}' character was found {value} times")
    print ("---End report---")



def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_string = text.lower()
    letters_dict = {}
    for c in lower_string:
        if c in letters_dict:
            letters_dict[c] += 1
        else:
            letters_dict[c] = 1
    return letters_dict


def sort_dict(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    new_dict = {}
    for key, value in sorted_dict.items():
        if key.isalpha():
            new_dict[key] = value
    return new_dict



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()