from flask import Flask
import mongoengine as me
from .controllers import user_bp
from .repositories import UserRepository

def create_app():

    app = Flask(__name__)

    mongo_connection = (
        'mongodb://root:'
        "abc123@"
        "localhost:27017"
    )
    me.connect(db="db", host=mongo_connection)
   
    user_repository = UserRepository()
    user_repository.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/users')

    return app
