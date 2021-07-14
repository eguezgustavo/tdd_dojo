from flask import Flask, jsonify
from flask_restx import Api
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

    from .endpoints.sum import api as namespace

    api.add_namespace(namespace)

    from .endpoints.sub import api as namespace

    api.add_namespace(namespace)

    from .endpoints.fac import api as namespace

    api.add_namespace(namespace)
        
    return app
