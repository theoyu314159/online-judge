from flask import Blueprint, current_app, request, abort
import mongoengine

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['POST'])
def register():
    
    try:
        current_app.user_repository.create(request.json['username'],request.json['password'])
    except mongoengine.errors.NotUniqueError:
        abort(400)

    return 'ok'
