from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, fav_color, fav_food, privileges):
        super().__init__(first_name, last_name, age, fav_color, fav_food)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        # print(f"{self.first_name} {self.last_name} has the following privileges:")
        # for privilege in self.privileges:
        #     print(f"\t {privilege}")
        self.privileges.show_privileges()
