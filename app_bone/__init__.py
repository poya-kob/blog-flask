from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_bone.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_mail import Mail
from celery import Celery

from .celery_conf import init_celery

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
ck_editor = CKEditor()
mail = Mail()


def create_app(config_class=Config, **kwargs):
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config_class)

    # Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ck_editor.init_app(app)
    mail.init_app(app)
    if kwargs.get("celery"):
        init_celery(kwargs.get("celery"), app)

    # bluePrints
    from app_bone.blog.routes import blog
    from app_bone.account.routes import user
    app.register_blueprint(blog)
    app.register_blueprint(user)
    return app


def make_celery(app_name=__name__):
    backend = "redis://localhost:6379/0"
    broker = backend.replace("0", "1")
    return Celery(app_name, backend=backend, broker=broker)


celery = make_celery()
