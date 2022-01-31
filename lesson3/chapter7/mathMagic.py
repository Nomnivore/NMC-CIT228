import random

problems = int(input("How many math problems would you like to practice?\n> "))
counter = 0
num_correct = 0
while counter < problems:
    rand1 = random.randrange(1, 1000)
    rand2 = random.randrange(1, 1000)
    correct_answer = rand1 + rand2
    your_answer = int(input(f"What is the value of {rand1} + {rand2} ?\n> "))
    if correct_answer == your_answer:
        print("Good job, you got it right!")
        num_correct += 1
    else:
        print(f"Bad answer! The correct answer is {correct_answer}.")
        
    counter += 1
    print()  # for spacing

print(f"You got {num_correct}/{problems} correct!")
print("Thanks for playing!")
