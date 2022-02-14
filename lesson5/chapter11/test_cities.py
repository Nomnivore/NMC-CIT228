import unittest
from city_functions import city_country


class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        city_formatted = city_country("santiago", "chile")
        self.assertEqual(city_formatted, "Santiago, Chile")

        city_formatted = city_country("detroit", "michigan")
        self.assertEqual(city_formatted, "Detroit, Michigan")

    def test_city_country_population(self):
        city_formatted = city_country("santiago", "chile", 5000000)
        self.assertEqual(
            city_formatted, "Santiago, Chile - population 5000000")

        city_formatted = city_country("detroit", "michigan", 1000000)
        self.assertEqual(
            city_formatted, "Detroit, Michigan - population 1000000")


if __name__ == "__main__":
    unittest.main()
