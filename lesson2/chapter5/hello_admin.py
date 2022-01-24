
print("----------- Exercise 5-8 where list has users -----------")
users = ["kyle", "jim", "admin", "jane", "bob"]
# users = []

if len(users) == 0:
    print("We need to find some users!")

for user in users:
    if user == "admin":
        print("Hello Administrator. Would you like to read today's report?")
    else:
        print(f"Hi {user.capitalize()}. Thank you for logging in again.")

print("----------- Exercise 5-9 where list is empty -----------")
# users = ["kyle", "jim", "admin", "jane", "bob"]
users = []

if len(users) == 0:
    print("We need to find some users!")

for user in users:
    if user == "admin":
        print("Hello Administrator. Would you like to read today's report?")
    else:
        print(f"Hi {user.capitalize()}. Thank you for logging in again.")
