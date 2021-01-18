class GasMileage:
    def __init__(self):
        self.totalMilesPerGallon = 0

    def calculate_gas_mileage(self, miles_driven, gallons_used):
        miles_per_gallon = miles_driven / gallons_used
        self.totalMilesPerGallon += miles_per_gallon
        return miles_per_gallon

    def get_total_miles_per_gallon(self):
        return self.totalMilesPerGallon
