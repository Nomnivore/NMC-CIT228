import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("John", "Smith", 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(1)
        self.assertEqual(self.employee.salary, 50001)


if __name__ == "__main__":
    unittest.main()
