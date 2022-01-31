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

print("------------ GLOSSARY ------------")
for key, val in glossary.items():
    print(f"  {key}")
    print(f"    {val}\n")

print("----------------------------------")
