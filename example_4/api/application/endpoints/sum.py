from flask_restx import Namespace, Resource, fields
from flask import jsonify

api = Namespace('/sum', description='Sum two numbers')

operation = api.model('Cat', {
    'id': fields.String(required=True, description='The operation identifier'),
    'operation': fields.String(required=True, description='The operation name'),
    'number_1': fields.Integer(required=True, description='First number'),
    'number_2': fields.Integer(required=False, description='Second number'),
    'result': fields.Integer(required=True, description='Result'),
})

OPERATIONS = { "id": 1, "operation": "sum", "number1": 1, "number2": 2, "result": 3 }


@api.route('/<int:number_1>/<int:number_2>')
@api.param('number_1', 'First number')
@api.param('number_2', 'Second number')
@api.response(404, 'Wrong parameters')
class Sum(Resource):
    @api.doc('do_sum')
    def get(self, number_1, number_2):
        '''Sum operation'''
        return jsonify(OPERATIONS)
