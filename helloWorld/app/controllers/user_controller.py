from app.repositories.user_repository import UserRepository

class UserController:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def create_user(name, email):
        return UserRepository.create_user(name, email)

    @staticmethod
    def update_user(user_id, name, email):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            return UserRepository.update_user(user, name, email)
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.delete_user(user)
            return True
        return False
