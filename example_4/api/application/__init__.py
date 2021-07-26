from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS

api = Api(
    version=1.0,
    title="Operations API",
    description="API for the Operations project",
)


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    config_module = f"application.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)

    @api.route('/hello')
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}
        
    return app
