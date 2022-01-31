def make_sandwich(bread, meat, *toppings):
    print(f"We are making you a {meat} sandwich on {bread} bread with the following toppings: ")
    for item in toppings:
        print(f"\t{item}")

make_sandwich("italian", "chicken salad", "celery", "onion", "cheddar cheese")
make_sandwich("cheese", "meatball", "pepper", "onion", "marinara", "onion")
make_sandwich("wheat", "veggie", "lettuce", "cucumber", "tomato", "olive", "spinach", "onion", "pepper")
