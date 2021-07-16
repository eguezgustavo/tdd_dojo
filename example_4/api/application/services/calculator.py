class Calculator:
   
    def sum(self, number_1, number_2):
        return number_1 + number_2
    
    def sub(self, number_1, number_2):
        return number_1 - number_2

    def fac(self, number):
        result = 1
        for positive_int in range(1, number + 1):
            result *= positive_int
        return result
