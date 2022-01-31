print("-------- Multiples of Ten --------")

num = int(
    input("Enter a number and I'll tell you if it's a multiple of 10 or not:\n> ")
    )

if num % 10 == 0:
    print(f"{num} is a multiple of 10!")
else:
    print(f"{num} is not a multple of 10.")
