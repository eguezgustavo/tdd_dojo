from flask_restx import Namespace, Resource, fields
from flask import jsonify
from application.repository.operations_repository import OperationsRepository
from application.services.calculator import Calculator
from application.services.presenter import OperationResultPersenter

api = Namespace('sum', description='Sum two numbers')

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
class Sum(Resource):
    @api.doc('do_sum')
    @api.marshal_with(operation)
    def get(self, number_1, number_2):
        '''Sum operation'''
        repository = OperationsRepository()
        calculator = Calculator(repository)
        presenter = OperationResultPersenter()

        result = calculator.sum(number_1, number_2)
        
        return presenter.get_json_response(result)

        # response = { "operation": "sum", "number1": number_1, "number2": number_2, "result": result }
        # id = database.save(response)

        # return { "id": id, "operation": "sum", "number1": number_1, "number2": number_2, "result": result }