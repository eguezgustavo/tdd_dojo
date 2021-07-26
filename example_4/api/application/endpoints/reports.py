from flask_restx import Namespace, Resource, fields
from application.repository.operations_repository import OperationsRepository

api = Namespace('/', description='Return an stored operation based on the id')

operation = api.model('result', {
    'id': fields.Integer(required=True, description='The operation identifier'),
    'operation': fields.String(required=True, description='The operation name'),
    'number_1': fields.Integer(required=True, description='First number'),
    'number_2': fields.Integer(required=True, description='Second number'),
    'result': fields.Integer(required=True, description='Result'),
})

@api.route('/<int:id>')
@api.param('id', 'operation id')
class Sum(Resource):
    @api.doc('return stored operation')
    def get(self, id):
        database = OperationsRepository()
        operation = database.query_by_id(id)
        '''Factorial operation'''
        return operation
