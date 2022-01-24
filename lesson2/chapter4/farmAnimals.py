animals = ["horse", "cow", "pig", "chicken", "rooster", "goat"]

more_animals = animals[:]

more_animals.append("sheep")
more_animals.append("llama")
more_animals.append("goose")
more_animals.append("duck")

print("----------- Original List -----------")
for animal in animals:
    print(animal)

print("\n----------- New List -----------")
for animal in more_animals:
    print(animal)

print(f"The first three items in the list are: {animals[:3]}")
print(f"Three items from the middle are: {more_animals[3:6]}")
print(f"The last three items are: {more_animals[-3:]}")
