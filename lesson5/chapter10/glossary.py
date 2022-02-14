import json
fname = "lesson5/chapter10/glossary.json"


glossary = {
    "if": "execute a code block only when a condition is true",
    "for": "iterate over a list, tuple or dictionary and execute a code block on each item",
    "import": "prepare some code from the stdlib, pypi package, or another project file for use in the current file",
    "f": "when placed immediately befora a double-quoted string, allows for interpolating values from the current scope",
    "not": "flips a boolean expression, allowing you to check if a statement is false",
    "in": "creates an iterator for lists, tuples and dictionaries. used with 'for' statements",
    "del": "removes an item from a list",
    "*": "unpacks a list into individual items",
    "elif": ""
}

# print("------------ GLOSSARY ------------")
# for key, val in glossary.items():
#     print(f"  {key}")
#     print(f"    {val}\n")

# print("----------------------------------")


def write_json():
    with open(fname, "w") as file:
        json.dump(glossary, file, indent=4, sort_keys=True)


def read_json():
    try:
        with open(fname, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found. Please choose another option.")
    else:
        for key, val in data.items():
            print(f" {key}: {val}")


def get_key():
    key = input("Enter the name of the term:\n> ")
    key = key.replace(" ", "_").lower()
    return key


def get_val(key):
    val = input(f"Enter the definition for {key}\n> ")
    return val


def append_json(data):
    try:
        with open(fname, "r+") as file:
            glossary_dict = json.load(file)
            glossary_dict.update(data)
            file.seek(0)
            json.dump(glossary_dict, file, indent=4, sort_keys=True)
    except FileNotFoundError:
        print("File not found. Please try again after saving the glossary.")
    else:
        print("Data successfully saved.")


def menu():
    print("Please choose an option:")
    print("\t1. Write glossary to file")
    print("\t2. Read from glossary file")
    print("\t3. Append to glossary file")
    print("\t4. -- Quit --")
    selection = int(input("> "))

    while selection not in [1, 2, 3, 4]:
        print("Invalid selection. Please try again.")
        selection = int(input("> "))
    return selection


choice = menu()
while choice != 4:
    if choice == 1:
        write_json()
    elif choice == 2:
        read_json()
    elif choice == 3:
        term = get_key()
        definition = get_val(term)
        append_json({term: definition})

    choice = menu()
