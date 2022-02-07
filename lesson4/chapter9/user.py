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
