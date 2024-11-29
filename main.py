def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    
    words = file_contents.split()
    sum_words = 0

    for word in words:
        sum_words += 1
    
    print("The number of words in this book =",sum_words)

main()