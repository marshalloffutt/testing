import unittest
from city_functions import get_full_name

class CitiesTestCase(unittest.TestCase):
    """Tests for 'get_full_name.py'."""

    def test_city_and_country(self):
        """Does 'London, England' work?"""
        full_name = get_full_name('london', 'england')
        self.assertEqual(full_name, 'London, England')

    def test_city_country_and_population(self):
        """Does 'London, England - population 8825000' work?"""
        full_name = get_full_name('london', 'england', 8825000)
        self.assertEqual(full_name, 'London, England - population 8825000')

unittest.main()
