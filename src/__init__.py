from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from config import Config
import os

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.config['SECRET_KEY'] = 'test_secret'

    return app