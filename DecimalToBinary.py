class Converter:
    def to_binary(self, decimal):
        binary = []

        if decimal > 1:
            self.to_binary(decimal // 2)
            # print(f" floor div :{decimal // 2}")
            # print(f"modulo op {decimal % 2}")
        print(decimal % 2, end='')

    def to_decimal(self, binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
