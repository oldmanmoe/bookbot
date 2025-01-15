
def main():    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    txt_count = len(get_word_count(text))
    char_count = character_count(text)
    
    print(f"~~~~~~ Begin report of {book_path} ~~~~~~\n")
    print(f"{txt_count} words were found in this document\n")
    
    for character in char_count:
        amount = char_count[character]
        print(f"The '{character}' character was found {amount} times")
    
    print("\n~~~~~~ End report ~~~~~")

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)

def get_word_count(text):
    words = text.split()
    return words

def character_count(word):
    char_dict ={}
    for char in word.lower():
        if char not in ('abcdefghijklmnopqrstuvwxyz'):
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return(char_dict)
    

if __name__ == "__main__":
    main()