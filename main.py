from gasMileage import GasMileage

gas_mileage = GasMileage()
sentinel = 1
while sentinel != -1:
    miles_string = input("Enter miles driven ")
    # print(type(miles_string))
    if int(miles_string) == -1:
        sentinel = -1
        break
    gallons_string = input("Enter gallons used")
    if int(gallons_string) == -1:
        sentinel = -1
        break
    miles_per_gallon = gas_mileage.calculate_gas_mileage(int(miles_string), int(gallons_string))
    print(f"Miles per gallon is {miles_per_gallon}")
    print(f"Total miles per gallon for all trips so far is: {gas_mileage.get_total_miles_per_gallon()}")
