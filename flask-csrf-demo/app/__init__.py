from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Insecure for demonstration only!

    # Enable CORS for all routes
    CORS(app, supports_credentials=True, origins=["http://localhost:8000"])

    # Configure session cookie settings
    app.config.update(
        SESSION_COOKIE_SAMESITE='None',  # Allow cross-origin cookies
        SESSION_COOKIE_SECURE=False,     # Disable Secure flag for HTTP
    )

    # Database configuration
    app.config['DATABASE'] = os.path.join(app.instance_path, 'users.db')

    # Ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Initialize the database only if it doesn't exist
    if not os.path.exists(app.config['DATABASE']):
        from app.models import init_db
        init_db(app)

    # Register routes
    from app.routes import register_routes
    register_routes(app)

    return app