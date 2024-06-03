from app.controllers.user_controller import UserController

class UserReport:
    @staticmethod
    def generate_report():
        return UserController.get_all_users()
