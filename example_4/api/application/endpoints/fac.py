from flask_restx import Namespace, Resource, fields
from application.services.calculator import Calculator
from application.repository.operations_repository import OperationsRepository

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
        calculator = Calculator()
        result = calculator.fac(number_1)
        response = { "operation": "fac", "number1": number_1, "number2": None, "result": result }
        database = OperationsRepository()
        id = database.save(response)

        return { "id": id, "operation": "fac", "number1": number_1, "number2": None, "result": result }
