class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served=1):
        self.number_served += number_served


panda_express = Restaurant('Panda Express', 'Chinese')

panda_express.describe_restaurant()
panda_express.open_restaurant()

print("---- 9.4 ----")

print(f"Starting number of served: {panda_express.number_served}")

panda_express.number_served = 5
print(f"Num served after changing: {panda_express.number_served}")

panda_express.set_number_served(10)
print(f"Num served after setting: {panda_express.number_served}")

panda_express.increment_number_served()
print(f"Num served after incrementing: {panda_express.number_served}")
