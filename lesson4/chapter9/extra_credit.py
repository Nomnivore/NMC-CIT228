from random import randint, choice


# 9.13
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Rolling a {self.sides}-sided die...")
        print(f"\t {randint(1, self.sides)}")


def die_rolls():
    six = Die()
    for i in range(10):
        six.roll_die()
    print("----\n")

    ten = Die(10)
    for i in range(10):
        ten.roll_die()
    print("----\n")

    twenty = Die(20)
    for i in range(10):
        twenty.roll_die()
    print("----\n")
   
    
# die_rolls()


# 9.14
class Lottery:
    def __init__(self):
        self.tokens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E"]

    def draw(self, num_tokens=4):
        winning = []
        for i in range(num_tokens):
            winning.append(choice(self.tokens))
        
        print(f"The winning tokens are: {winning}")
        return winning


def lottery_draws():
    lotto = Lottery()
    
    my_ticket = ["A", 2, 5, 9]
    winning_ticket = []
    draws = 0

    while my_ticket != winning_ticket:
        draws += 1
        winning_ticket = lotto.draw()
    
    print(f"After {draws} plays, I've finally won!")




lottery_draws()
# low: 583
# high: 122520


