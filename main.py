import string

book_path = "books/frankenstein.txt"

def get_book_path(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join(x for x in text if x.isalpha())
    letter_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter_dict:
            letter_dict[lowered] += 1
        else:
            letter_dict[lowered] = 1
    return letter_dict

def report(letter_dict):
    lst = list(letter_dict.items())
    lst.sort()
    for i in lst:
        print(f"The '{i[0]}' character was found {i[1]} times")

def main():
    text = get_book_path(book_path)
    number_of_words = count_words(text)
    print("--- Begin report of books/frankenstein.txt ---\n"
    f"{number_of_words} are found in the document\n""")
    letters = count_letters(text)
    report(letters)
    print("--- End report ---\n")

main()

