def main():
    location = "books/frankenstein.txt"
    text = book_text(location)
    sum_words = get_sum_words(text)
    character_dict = get_character_count(text)
    character_dict_sorted = dictionary_to_sorted_list(character_dict)
    print("-- Report of", location,"--")
    print("The number of words in this book =",sum_words)
    print()

    for character in character_dict_sorted:
        if character["char"].isalpha() == True:
            print("The '",character["char"],"' character was found",character["num"],"times")
        continue

    print("-- End of report --")

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

def sort_on(dict):
    return dict["num"]

def dictionary_to_sorted_list(character_dict):
    character_dict_sorted = []
    for character in character_dict:
        character_dict_sorted.append({"char": character, "num": character_dict[character]})
    character_dict_sorted.sort(reverse=True, key=sort_on)
    return character_dict_sorted

main()