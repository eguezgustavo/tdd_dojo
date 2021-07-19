from flask_restx import Namespace, Resource, fields
from application.services.calculator import Calculator
from application.repository.operations_repository import OperationsRepository
from application.services.presenter import OperationResultPersenter


api = Namespace('fac', description='Return the factorial of two numbers')

operation = api.model('result', {
    'id': fields.Integer(required=True, description='The operation identifier'),
    'operation': fields.String(required=True, description='The operation name'),
    'number1': fields.Integer(required=True, description='First number'),
    'number2': fields.Integer(required=True, description='First number'),
    'result': fields.Integer(required=True, description='Result'),
})

@api.route('/<int:number_1>')
@api.param('number_1', 'First number')
@api.response(404, 'Wrong parameters')
class Fac(Resource):
    @api.doc('do_factorial')
    @api.marshal_with(operation)
    def get(self, number_1):
        '''Factorial operation'''
        repository = OperationsRepository()
        calculator = Calculator(repository)
        presenter = OperationResultPersenter()

        result = calculator.fac(number_1)
        
        return presenter.get_json_response(result)
