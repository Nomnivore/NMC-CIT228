class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served=1):
        self.number_served += number_served


print("---- 9.6 ----")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(
            f"The following flavors are available: {', '.join(self.flavors)}")


dairy = IceCreamStand("Main St Ice Cream", "Dairy", [
                      "chocolate", "vanilla", "strawberry"])

dairy.describe_restaurant()

dairy.show_flavors()
