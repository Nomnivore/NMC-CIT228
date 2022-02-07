from restaurant import Restaurant
from icecream import IceCreamStand

panda_express = Restaurant('Panda Express', 'Chinese')

panda_express.describe_restaurant()
panda_express.open_restaurant()
print(f"Starting number of served: {panda_express.number_served}")

panda_express.number_served = 5
print(f"Num served after changing: {panda_express.number_served}")

panda_express.set_number_served(10)
print(f"Num served after setting: {panda_express.number_served}")

panda_express.increment_number_served()
print(f"Num served after incrementing: {panda_express.number_served}")

print("\n-------------------\n")

dairy = IceCreamStand("Main St Ice Cream", "Dairy", [
                      "chocolate", "vanilla", "strawberry"])

dairy.describe_restaurant()

dairy.show_flavors()
