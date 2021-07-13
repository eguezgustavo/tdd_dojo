from flask import Flask, jsonify
from flask_restx import Api

api = Api(
    version=1.0,
    title="Operations API",
    description="API for the Operations project",
)


def create_app(config_name):

    app = Flask(__name__)

    api = Api(app)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    from .endpoints.operations import api as namespace

    api.add_namespace(namespace)
        
    return app
