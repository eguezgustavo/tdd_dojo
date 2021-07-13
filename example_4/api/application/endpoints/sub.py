from flask_restx import Namespace, Resource, fields
from application.services.calculator import Calculator

api = Namespace('sub', description='Subctract two numbers')

operation = api.model('result', {
    'id': fields.String(required=True, description='The operation identifier'),
    'operation': fields.String(required=True, description='The operation name'),
    'number_1': fields.Integer(required=True, description='First number'),
    'number_2': fields.Integer(required=False, description='Second number'),
    'result': fields.Integer(required=True, description='Result'),
})

OPERATIONS = { "id": 1, "operation": "sub", "number1": 5, "number2": 2, "result": 3 }
@api.route('/<int:number_1>/<int:number_2>')
@api.param('number_1', 'First number')
@api.param('number_2', 'Second number')
@api.response(404, 'Wrong parameters')
class Sum(Resource):
    @api.doc('do_sum')
    def get(self, number_1, number_2):
        '''Sub operation'''
        calculator = Calculator()
        result = calculator.sub(number_1, number_2)

        return { "id": 1, "operation": "sub", "number1": number_1, "number2": number_2, "result": result }

