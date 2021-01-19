class SalesCommissionCalculator:
    def __init__(self):
        self.item_prices = {1: 239.99, 2: 129.75, 3: 99.95, 4: 350.89}

    def calculate_value(self, item_number, number_sold):
        item_value = self.item_prices.get(item_number, -1)
        base_pay = 200
        earnings = 0 + base_pay
        if item_value != -1:
            earnings = number_sold * item_value + base_pay
        return int(earnings)

    def get_item_value(self, item_no):
        return self.item_prices.get(item_no, -1)
