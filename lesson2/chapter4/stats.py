import random

print("------------ Hands on 2 ------------")

number = random.randrange(10, 100)

numbers = list(range(number))

print(numbers)

print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")
print(f"Total of all numbers: {sum(numbers)}")
print(f"The average number: {sum(numbers) / len(numbers)}")
