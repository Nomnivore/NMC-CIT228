import random

print("---- Welcome to the additions quiz! ----")
counter = 0
num_correct = 0
num_incorrect = 0
while counter < 10:
    rand1 = random.randrange(1, 1000)
    rand2 = random.randrange(1, 1000)
    correct_answer = rand1 + rand2
    your_answer = int(input(f"What is the value of {rand1} + {rand2} ?\n> "))
    if correct_answer == your_answer:
        print("Good job, you got it right!")
        num_correct += 1
    else:
        print(f"Bad answer! The correct answer is {correct_answer}.")
        num_incorrect += 1
    
    counter += 1
    print()  # for spacing
    if num_incorrect > 5:
        print("Too many incorrect answers. I recommend you seek help from a tutor.\n")
        break
        

print(f"You got {num_correct}/{counter} correct!")
print("Thanks for playing!")
