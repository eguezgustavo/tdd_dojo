from application.repository.operations_repository import OperationsRepository


class Calculator:

    def __init__(self, repository: OperationsRepository) -> None:
        self.repository = repository

    def save_on_repository(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            self = args[0]
            number_1 = args[1]
            number_2 = args[2]
            result = { "operation": func.__name__, "number1": number_1, "number2": number_2, "result": res }
            return self.repository.save(result)
        return wrapper
    
    @save_on_repository
    def sum(self, number_1, number_2):
        return number_1 + number_2
    
    @save_on_repository
    def sub(self, number_1, number_2):
        return number_1 - number_2

    @save_on_repository
    def fac(self, number_1, number_2):
        result = 1
        for positive_int in range(1, number_1 + 1):
            result *= positive_int
        return result
