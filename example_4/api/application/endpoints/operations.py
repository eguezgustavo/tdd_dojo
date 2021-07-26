from flask_restx import Namespace, Resource, fields
from ..repository.operations_repository import OperationsRepository
from ..services.calculator import Calculator
from ..services.presenter import OperationResultPersenter

api = Namespace('operations', description='Do sum, sub or fac')

operation = api.model('result', {
    'id': fields.Integer(required=True, description='The operation identifier'),
    'operation': fields.String(required=True, description='The operation name'),
    'number1': fields.Integer(required=True, description='First number'),
    'number2': fields.Integer(required=False, description='Second number'),
    'result': fields.Integer(required=True, description='Result'),
})

def do_operation(operation, number_1, number_2 = None):
    '''Do operation'''
    repository = OperationsRepository()
    calculator = Calculator(repository)
    presenter = OperationResultPersenter()

    result = getattr(calculator, operation)(number_1, number_2)
    
    return presenter.get_json_response(result)

@api.route('/sum/<int:number_1>/<int:number_2>')
@api.param('number_2', 'Second number')
@api.param('number_1', 'First number')
@api.response(404, 'Wrong parameters')
class Sum(Resource):
    @api.doc('do_sum')
    @api.marshal_with(operation)
    def get(self, number_1, number_2):
       
        return do_operation('sum', number_1, number_2)


@api.route('/sub/<int:number_1>/<int:number_2>')
@api.param('number_2', 'Second number')
@api.param('number_1', 'First number')
@api.response(404, 'Wrong parameters')
class Sub(Resource):
    @api.doc('do_sum')
    @api.marshal_with(operation)
    def get(self, number_1, number_2):
       
        return do_operation('sub', number_1, number_2)


@api.route('/fac/<int:number_1>')
@api.param('number_1', 'First number')
@api.response(404, 'Wrong parameters')
class Fac(Resource):
    @api.doc('do_sum')
    @api.marshal_with(operation)
    def get(self, number_1):
       
        return do_operation('fac', number_1)
