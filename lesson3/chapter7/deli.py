sandwich_orders = ["ham", "turkey", "veggie", "pastrami", "salami",
                   "tuna", "pastrami", "chicken bacon", "pastrami",
                   "meatball", "steak"]

finished_sandwiches = []

print("----- Sandwich Shop -----")
print("Sorry, but we have run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("----- Making orders -----")
while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"I have finished making your {order} sandwich.")
    finished_sandwiches.append(order)
