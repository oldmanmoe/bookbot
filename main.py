
def main():    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    txt_count = len(get_word_count(text))
    print("Text: ",text)
    print("Word Count: ",txt_count)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return(file_contents)

def get_word_count(text):
    words = text.split()
    return words

#Add a new function to your script that takes the text from the book as a string,
# and returns the number of times each character appears in the string. 
# Convert any character to lowercase, we don't want duplicates.
        
if __name__ == "__main__":
    main()