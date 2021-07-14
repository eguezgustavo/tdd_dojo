from flask_restx import Namespace, Resource, fields

api = Namespace('fac', description='Subctract two numbers')


@api.route('/<int:number_1>')
@api.param('number_1', 'First number')
@api.response(404, 'Wrong parameters')
class Sum(Resource):
    @api.doc('do_factorial')
    def get(self, number_1):
        '''Factorial operation'''
        return ''
