from flask_restx import Namespace, Resource, fields

api = Namespace('/sub', description='Subctract two numbers')


@api.route('/<int:number_1>/<int:number_2>')
@api.param('number_1', 'First number')
@api.param('number_2', 'Second number')
@api.response(404, 'Wrong parameters')
class Sum(Resource):
    @api.doc('do_sum')
    def get(self, number_1, number_2):
        '''Sum operation'''
        return 'sub'
