print("--------------- Hands on 1 ---------------")
foods = ["brisket", "monte cristo", "cheesecake", "pizza", "sushi", "tacos"]
print(f"Favorite foods: {foods}")

numbers = [7, 3, 14, 50, 36, 21]
print(f"Lucky numbers: {numbers}")

movies = ["Thor: Ragnarok", "Deadpool 2", "Free Guy"]
print(f"Favorite movies: {movies}")

everything = [
    *foods[:2],
    *numbers[:2],
    *movies[:2]
]
print(f"Combo list: {everything}")

print(f"Last food item: {foods[-1]}")

print(f"2nd, 4th, and 6th numbers: {numbers[1]}, {numbers[3]}, {numbers[5]}")

print(f"All movies: {movies[0]}, {movies[1]}, {movies[2]}")

print(f"Firsts: {everything[0]}, {everything[2]}, {everything[4]}")

print("--------------- Hands on 2 ---------------")
movies.append("Baby Driver")
print(f"Added movie: {movies}")

numbers.insert(3, 52)
print(f"Added number at sub 3: {numbers}")

foods.insert(5, "frappuccino")
print(f"Added food at sub 5: {foods}")

del foods[3]
print(f"Deleted food[3]: {foods}")

numbers.pop()
print(f"Deleted last number: {numbers}")

numbers.pop(2)
print(f"Deleted number at sub 2: {numbers}")

print("--------------- Hands on 3 ---------------")
movies.sort()
print(f"Sorted movies: {movies}")

foods.sort()
print(f"Sorted foods: {foods}")

print(f"Temp sorted numbers: {sorted(numbers)}")
print(f"Unsorted numbers: {numbers}")

movies.reverse()

print(f"Reversed movies: {movies}")


print("--------------- Chapter 4, Hands on 1 ---------------")

print("\nFood list")
print("---------------------------")
for food in foods:
    print(food)

print("\nNumber list")
print("---------------------------")
for number in numbers:
    print(number)

print("\nMovie list")
print("---------------------------")
for movie in movies:
    print(movie)

print("\nCombo list")
print("---------------------------")
for item in everything:
    print(item)
