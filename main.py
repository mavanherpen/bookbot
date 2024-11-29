def main():
    location = "books/frankenstein.txt"
    text = book_text(location)
    sum_words = get_sum_words(text)
    character_dict = get_character_count(text)
    print("The number of words in this book =",sum_words)
    print(character_dict)

def book_text(location):    
    with open(location) as f:
        return f.read()

def get_sum_words(text):
    sum_words = 0
    words = text.split()
    for word in words:
        sum_words += 1
    return sum_words

def get_character_count(text):
    lowered_text = text.lower()
    character_dict = {}
    
    for character in lowered_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

main()