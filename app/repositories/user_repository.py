from ..models import User

class UserRepository:

    def init_app(self, app):
        app.user_repository = self

    def create(self, username, password):
        user = User(username=username, password=password)
        user.save()
        return user.id
