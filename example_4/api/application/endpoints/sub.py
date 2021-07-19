from flask_restx import Namespace, Resource, fields
from application.repository.operations_repository import OperationsRepository
from application.services.calculator import Calculator
from application.services.presenter import OperationResultPersenter


api = Namespace('sub', description='Subctract two numbers')

operation = api.model('result', {
    'id': fields.Integer(required=True, description='The operation identifier'),
    'operation': fields.String(required=True, description='The operation name'),
    'number1': fields.Integer(required=True, description='First number'),
    'number2': fields.Integer(required=False, description='Second number'),
    'result': fields.Integer(required=True, description='Result'),
})

@api.route('/<int:number_1>/<int:number_2>')
@api.param('number_1', 'First number')
@api.param('number_2', 'Second number')
@api.response(404, 'Wrong parameters')
class Sub(Resource):
    @api.doc('do_subctract')
    @api.marshal_with(operation)
    def get(self, number_1, number_2):
        '''Sub operation'''
        repository = OperationsRepository()
        calculator = Calculator(repository)
        presenter = OperationResultPersenter()

        result = calculator.sub(number_1, number_2)
        
        return presenter.get_json_response(result)
