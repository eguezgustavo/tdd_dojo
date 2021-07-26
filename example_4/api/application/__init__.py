from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from .repository.models import db, OperationModel, migrate
from .endpoints.operations import api as operations_namespace
from .endpoints.reports import api as reports_namespace

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

    db.init_app(app)
    migrate.init_app(app, db)

    api.add_namespace(operations_namespace)
    api.add_namespace(reports_namespace)
        
    return app
