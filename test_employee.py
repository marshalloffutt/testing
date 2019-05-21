import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.larry = Employee('larry', 'whizbang', 60000)

    def test_give_default_raise(self):
        """Test to see if Larry gets his 5000 raise."""
        self.larry.give_raise()
        self.assertEqual(self.larry.salary, 65000)

    def test_give_gustom_raise(self):
        """Test to see if we can give Larry double his salary."""
        self.larry.give_raise(60000)
        self.assertEqual(self.larry.salary, 120000)

unittest.main()