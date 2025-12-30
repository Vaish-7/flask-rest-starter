from flask import Flask
from .config import Config
from .db import init_db
from .auth import jwt
from .routes.items import items_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    jwt.init_app(app)
    app.register_blueprint(items_bp, url_prefix="/api/v1/items")
    @app.route("/")
    def root():
        return {"message": "Welcome to Flask REST Starter"}
    return app