from user import User
from admin import Admin
# from privileges import Privileges  # unused

first = User("John", "Doe", 25, "blue", "pizza")
second = User("Jane", "Smith", 33, "green", "icecream")
third = User("Alex", "Andrews", 22, "orange", "salad")

for user in [first, second, third]:
    user.describe_user()
    user.greet_user()
    print("--------\n")

print("---- 9.5 ----")
for i in range(3):
    first.increment_login_attempts()

print(f"Number of login attempts: {first.login_attempts}")
first.reset_login_attempts()
print(f"Number of login attempts after reset: {first.login_attempts}")


admin = Admin("Lorem", "Ipsum", 41, "red", "steak", [
              "can add post", "can delete post", "can ban user"])

admin.show_privileges()
