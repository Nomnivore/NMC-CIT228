fname = "lesson5/chapter10/guest.txt"
fbook = "lesson5/chapter10/guest_book.txt"

# 10-3
name = input("Enter your name\n> ")

with open(fname, "w") as file:
    file.write(name)


# 10-4
print("---- 10-4 ----")
while True:
    name = input("Enter your name (or 'q' to quit):\n> ")
    if name == 'q':
        break

    with open(fbook, "a") as book:
        book.write(name + "\n")
