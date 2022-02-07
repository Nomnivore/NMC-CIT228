class User:
    def __init__(self, first_name, last_name, age, fav_color, fav_food):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fav_color = fav_color
        self.fav_food = fav_food
        self.login_attempts = 0

    def describe_user(self):
        print(f"Their name is {self.first_name} {self.last_name}. They are {self.age} years old and their favorite color is {self.fav_color}. They love {self.fav_food}.")

    def greet_user(self):
        print(
            f"Welcome, {self.first_name}! I've got a fresh batch of {self.fav_color} {self.fav_food} waiting for you.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


first = User("John", "Doe", 25, "blue", "pizza")
second = User("Jane", "Smith", 33, "green", "icecream")
third = User("Alex", "Andrews", 22, "orange", "salad")

for user in [first, second, third]:
    user.describe_user()
    user.greet_user()
    print("--------\n")

print("---- 9.5 ----")
for i in range(3):
    first.increment_login_attempts()

print(f"Number of login attempts: {first.login_attempts}")
first.reset_login_attempts()
print(f"Number of login attempts after reset: {first.login_attempts}")
