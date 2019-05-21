class Employee():
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, salary):
        """Constructor for the employee."""
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = salary

    def give_raise(self, pay_increase=5000):
        """Increase employee salary"""
        self.salary = self.salary + pay_increase
        # Can't use 'raise' because it is a reserved Python keyword
