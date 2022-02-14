
keepPlaying = ""
while keepPlaying != "q":
    num1 = input("Enter #1:\n> ")
    num2 = input("Enter #2:\n> ")

    try:
        num1 = int(num1)
        num2 = int(num2)
        added = num1 + num2
    except ValueError:
        print("Looks like you've entered letters instead of numbers.")
    else:
        print(f"{num1} + {num2} = {added}")
    finally:
        keepPlaying = input("Would you like to keep playing? q to quit:\n> ")
