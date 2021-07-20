from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sys

api = Api(
    version=1.0,
    title="Operations API",
    description="API for the Operations project",
)

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    CORS(app)

    api = Api(app)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    db.init_app(app)

    from application.repository.models import OperationModel, migrate

    migrate.init_app(app, db)

    from .endpoints.sum import api as namespace

    api.add_namespace(namespace)

    from .endpoints.sub import api as namespace

    api.add_namespace(namespace)

    from .endpoints.fac import api as namespace

    api.add_namespace(namespace)

    from .endpoints.reports import api as namespace

    api.add_namespace(namespace)
        
    return app
