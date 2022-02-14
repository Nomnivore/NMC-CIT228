import unittest
from restaurant import Restaurant


class RestaurantTest(unittest.TestCase):
    """Tests for 'restaurant.py'"""

    def setUp(self):
        self.restaurant = Restaurant("Qdoba", "Mexican")

    def test_restaurant_name(self):
        self.assertEqual(self.restaurant.restaurant_name, "Qdoba")

    def test_set_number_served(self):
        self.restaurant.set_number_served(10)
        self.assertEqual(self.restaurant.number_served, 10)

    def test_increment_number_served(self):
        self.restaurant.number_served = 15
        self.restaurant.increment_number_served()
        self.assertEqual(self.restaurant.number_served, 16)


if __name__ == "__main__":
    unittest.main()
