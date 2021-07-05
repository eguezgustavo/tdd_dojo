class Calculator:

    def __init__(self, calculator):
        self.calculator = calculator
    
    def sum(self, number_1, number_2):
        result = self.calculator.sum(number_1, number_2)
        if result > 100:
            return "OverflowError"
        return result
    
    def sub(self, number_1, number_2):
        return self.calculator.sum(number_1, - number_2)

    def fac(self, number):
        result = 1
        for positive_int in range(1, number + 1):
            result = self.calculator.mul(result, positive_int)
        return result
