from application.repository.models import OperationModel
    
def test__OperationModel__can_be_instantiated__given_valid_arguments():
    valid_arguments =  { "operation": "sum", "number1": 1, "number2": 1, "result": 2 }

    operation = OperationModel(**valid_arguments)
    
    assert operation.operation == 'sum'
    assert operation.number1 == 1
    assert operation.number2 == 1
    assert operation.result == 2
