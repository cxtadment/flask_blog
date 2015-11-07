from flask import Flask
from flask.ext.login import LoginManager
from app.admin import create_admin
from app.models import db, User
from app.views import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    init_login(app)
    register_blueprints(app)
    register_database(app)
    create_admin(app)

    return app


def register_blueprints(app):
    app.register_blueprint(bp)


def register_database(app):
    db.init_app(app)


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()
