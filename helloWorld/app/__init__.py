from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    api = Api(app)
    from app.resources.user_resource import UserResource, UserListResource, UserReportResource
    api.add_resource(UserListResource, '/api/users')
    api.add_resource(UserResource, '/api/users/<int:id>')
    api.add_resource(UserReportResource, '/api/users/report')

    with app.app_context():
        db.create_all()

    return app
