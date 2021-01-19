from gasMileage import GasMileage
from SalesCommisionCalculator import SalesCommissionCalculator
from salaryCalculator import SalaryCalculator

# gas_mileage = GasMileage()
# sentinel = 1
# while sentinel != -1:
#     miles_string = input("Enter miles driven ")
#     # print(type(miles_string))
#     if int(miles_string) == -1:
#         sentinel = -1
#         break
#     gallons_string = input("Enter gallons used")
#     if int(gallons_string) == -1:
#         sentinel = -1
#         break
#     miles_per_gallon = gas_mileage.calculate_gas_mileage(int(miles_string), int(gallons_string))
#     print(f"Miles per gallon is {miles_per_gallon}")
#     print(f"Total miles per gallon for all trips so far is: {gas_mileage.get_total_miles_per_gallon()}")

# sales_commission_calculator = SalesCommissionCalculator()
# sentinel = 1
# while sentinel != -1:
#     item_number_string = input("Enter item number or -1 to quit ")
#     item_number = int(item_number_string)
#     if item_number == -1:
#         sentinel = -1
#         break
#     item_quantity_string = input("Enter number of items sold or -1 to quit ")
#     item_quantity = int(item_quantity_string)
#     if item_quantity == -1:
#         sentinel = -1
#         break
#     earnings = sales_commission_calculator.calculate_value(item_number, item_quantity)
#     print(f"Earnings are {earnings}")

sentinel = 1
while sentinel != -1:
    hours_string = input("Enter hours worked or -1 to quit")
    hours = int(hours_string)
    if hours == -1:
        sentinel = -1
        break
    rates_string = input("Enter hourly rates or -1 to quit")
    rates = float(rates_string)
    if int(rates) == -1:
        sentinel = -1
        break
    salary = SalaryCalculator.calculate_salary(hours, rates)
    print(f"Salary is {salary}")
