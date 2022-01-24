users = ["Kyle", "Jim", "Admin", "Jane", "Bob"]

new_users = ["Eric", "Bob", "Sean", "Mary"]

lower_users = [user.lower() for user in users]

for new in new_users:
    if new.lower() in lower_users:
        print(f"{new} has already been taken - please choose another username.")
    else:
        print(f"{new} is available!")
