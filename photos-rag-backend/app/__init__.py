# __init__.py
from flask import Flask  # Corrected import statement
from flask_cors import CORS
from .config import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    """
    Create a Flask app using the provided configuration class.
    Input: config_class--The configuration class to use.
    Return: A Flask app.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask CORS
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Import and register blueprints or routes
    from .routes import main as main_blueprint  # Ensure this import matches your project structure
    app.register_blueprint(main_blueprint)

    return app
