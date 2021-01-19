from unittest import TestCase
from salaryCalculator import SalaryCalculator


class TestSalaryCalculator(TestCase):

    def test_calculate_salary(self):
        self.assertEqual(2000, SalaryCalculator.calculate_salary(20, 100))
        self.assertEqual(7000, SalaryCalculator.calculate_salary(60, 100))
