from flask import Flask
import mongoengine as me
from .controllers import user_bp, login_bp
from .repositories import UserRepository
from .services import AuthService

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f"config.{config_name.capitalize()}Config")

    mongo_connection = (
        'mongodb://root:'
        "abc123@"
        "localhost:27017"
    )
    me.connect(db="db", host=mongo_connection)
    user_repository = UserRepository()
    user_repository.init_app(app)

    auth_service = AuthService()
    auth_service.init_app(app, app.config.get('JWT_SECRET'))

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(login_bp, url_prefix='/login')

    return app
