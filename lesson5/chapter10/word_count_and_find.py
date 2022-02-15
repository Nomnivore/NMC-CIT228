def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


def find_words(filename, search):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents = contents.lower()
        search = search.lower()
        words = contents.count(search)
        print(
            f"The word '{search}' occured {words} times in the file {filename}.")


filenames = ["lesson5/chapter10/LOTR1.txt",
             "lesson5/chapter10/LOTR2.txt", "lesson5/chapter10/LOTR3.txt"]
for filename in filenames:
    count_words(filename)

search_word = input("Enter a word to search for:\n> ")

if search_word:
    for filename in filenames:
        find_words(filename, search_word)
