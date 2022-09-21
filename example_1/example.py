class Calculator:
    def add(self, first_number, second_number):
        if not isinstance(first_number, int) or not isinstance(second_number, int):
            raise TypeError("Input shouldn be numbers")
        if first_number < 0 or second_number < 0:
            raise ValueError("A number shouldn't be negative")
        return first_number + second_number
