from flask import request, render_template
from flask_restful import Resource
from app.controllers.user_controller import UserController

class UserListResource(Resource):
    def get(self):
        users = UserController.get_all_users()
        return [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

    def post(self):
        data = request.get_json()
        user = UserController.create_user(name=data['name'], email=data['email'])
        return {'id': user.id, 'name': user.name, 'email': user.email}, 201

class UserResource(Resource):
    def get(self, id):
        user = UserController.get_user_by_id(id)
        if user:
            return {'id': user.id, 'name': user.name, 'email': user.email}
        return {'message': 'User not found'}, 404

    def put(self, id):
        data = request.get_json()
        user = UserController.update_user(user_id=id, name=data['name'], email=data['email'])
        if user:
            return {'id': user.id, 'name': user.name, 'email': user.email}
        return {'message': 'User not found'}, 404

    def delete(self, id):
        if UserController.delete_user(id):
            return {'message': 'User deleted'}, 204
        return {'message': 'User not found'}, 404

class UserReportResource(Resource):
    def get(self):
        users = UserController.get_all_users()
        return render_template('user_report.html', users=users)
