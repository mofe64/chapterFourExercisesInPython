class SalaryCalculator:
    @staticmethod
    def calculate_salary(hours, hourly_rate):
        if hours <= 40:
            return hours * hourly_rate
        if hours > 40:
            base_pay = hourly_rate * 40
            extra_time = hours - 40
            extra_time_pay = (hourly_rate * 1.5) * extra_time
            return base_pay + extra_time_pay
