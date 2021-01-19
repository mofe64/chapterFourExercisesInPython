from unittest import TestCase
from SalesCommisionCalculator import SalesCommissionCalculator


class TestSalesCommissionCalculator(TestCase):

    def setUp(self) -> None:
        self.sales_commission_calculator = SalesCommissionCalculator()

    def tearDown(self) -> None:
        self.sales_comission_calculator = None

    def test_calculate_value(self):
        self.assertEqual(3708, self.sales_commission_calculator.calculate_value(4, 10))

    def test_get_item_value(self):
        self.assertEqual(239.99, self.sales_commission_calculator.get_item_value(1))
        self.assertEqual(129.75, self.sales_commission_calculator.get_item_value(2))
        self.assertEqual(99.95, self.sales_commission_calculator.get_item_value(3))
        self.assertEqual(350.89, self.sales_commission_calculator.get_item_value(4))
        self.assertEqual(-1, self.sales_commission_calculator.get_item_value(100))
