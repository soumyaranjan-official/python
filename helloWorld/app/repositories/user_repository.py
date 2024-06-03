from app import db
from app.models.user import User

class UserRepository:
    @staticmethod
    def create_user(name, email):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user, name, email):
        user.name = name
        user.email = email
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
