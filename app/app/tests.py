"""
Testing calculator functions
"""

from django.test import SimpleTestCase
from app import calculator


class CalculatorTests(SimpleTestCase):

    def test_add_numbers(self):
        """
        Testing add function from calculator
        """

        result = calculator.add(1, 2)

        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """
        Testing subtract function from calculator
        """

        result = calculator.subtract(5, 2)

        self.assertEqual(result, 3)
