class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print(f"\t {privilege}")
