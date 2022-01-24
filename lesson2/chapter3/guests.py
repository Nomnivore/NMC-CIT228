print("--------------- Exercise 3.4 ---------------")

guests = ["Kitboga", "Stan Lee", "Noel Miller"]

print(f"{guests[0]}, can you make it to dinner this Saturday?")
print(f"{guests[1]}, can you make it to dinner this Saturday?")
print(f"{guests[2]}, can you make it to dinner this Saturday?")

print("--------------- Exercise 3.5 ---------------")

print(f"{guests[0]} cannot make it to the dinner this Saturday.")
guests[0] = "Jim Browning"

print(f"{guests[0]}, can you make it to dinner this Saturday?")
print(f"{guests[1]}, can you make it to dinner this Saturday?")
print(f"{guests[2]}, can you make it to dinner this Saturday?")

print("--------------- Exercise 3.6 ---------------")

guests = ["Kitboga", "Stan Lee", "Noel Miller"]
guests.insert(0, "John Smith")
guests.insert(2, "Mary Sue")
guests.append("Jim Bob")

print("I found a bigger dinner table on Craigslist and will have it by Thursday.")

print(f"I am inviting a total of {len(guests)} guests to dinner. (E3.9)")

print(f"{guests[0]}, can you make it to dinner this Saturday?")
print(f"{guests[1]}, can you make it to dinner this Saturday?")
print(f"{guests[2]}, can you make it to dinner this Saturday?")
print(f"{guests[3]}, can you make it to dinner this Saturday?")
print(f"{guests[4]}, can you make it to dinner this Saturday?")
print(f"{guests[5]}, can you make it to dinner this Saturday?")

print("--------------- Exercise 3.7 ---------------")

guests = ["Kitboga", "Stan Lee", "Noel Miller"]
guests.insert(0, "John Smith")
guests.insert(2, "Mary Sue")
guests.append("Jim Bob")

print("Unfortunately, the table will be late and I can only invite two people to dinner.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner this Saturday.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner this Saturday.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner this Saturday.")
print(f"Sorry {guests.pop()}, I can't invite you to dinner this Saturday.")

print(f"{guests[0]}, can you make it to dinner this Saturday?")
print(f"{guests[1]}, can you make it to dinner this Saturday?")
