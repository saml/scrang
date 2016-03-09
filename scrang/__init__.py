from flask import Flask

from .views import bp as default_views


def create_app():
    app = Flask(__name__)
    app.register_blueprint(default_views)
    return app
