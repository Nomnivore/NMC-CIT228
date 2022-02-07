class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


panda_express = Restaurant('Panda Express', 'Chinese')

five_guys = Restaurant("Five Guys", "American")

qdoba = Restaurant("Qdoba", "Mexican")

print("---- List of Restaurants (9.1) ----")
panda_express.describe_restaurant()
five_guys.describe_restaurant()
qdoba.describe_restaurant()

print("---- 9.2 ----")
panda_express.open_restaurant()
five_guys.open_restaurant()
qdoba.open_restaurant()
