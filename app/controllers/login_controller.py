from flask import Blueprint, current_app, request, abort
import bcrypt

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['POST'])

def login():
    username=request.json['username']
    password=request.json['password']
    hashed_password = current_app.user_repository.get(username).password
    password_bytes = password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    profile={'username' : username ,'role' : 'user' }
    if  bcrypt.checkpw(password_bytes, hashed_bytes):
        return current_app.auth_service.issue_token(profile)
    abort(401)
