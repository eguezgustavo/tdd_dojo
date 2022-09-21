class Calculator:
    def add(self, first_number, second_number):
        if first_number < 0 or second_number < 0:
            raise ValueError("A number shouldn't be negative")
        return first_number + second_number
