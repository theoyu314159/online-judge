from flask import Blueprint, current_app, request, abort
import mongoengine
import bcrypt

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['POST'])
def register():

    try:
        password=request.json['password']
        password_bytes = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        current_app.user_repository.create(request.json['username'], hashed.decode('utf-8'))
    except mongoengine.errors.NotUniqueError:
        abort(409)

    return 'ok'
