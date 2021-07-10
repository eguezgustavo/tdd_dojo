from flask import Flask, jsonify


def create_app(config_name):

    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    @app.route("/hello")
    def hello():
        return jsonify({'hello':'world'})
        
    return app
