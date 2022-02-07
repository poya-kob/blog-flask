from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_bone.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_mail import Mail
from celery import Celery

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
ck_editor = CKEditor()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config_class)

    # Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ck_editor.init_app(app)
    mail.init_app(app)

    # bluePrints
    from app_bone.blog.routes import blog
    from app_bone.account.routes import user
    app.register_blueprint(blog)
    app.register_blueprint(user)
    return app


def make_celery(app=None):
    app = app or create_app()
    async_celery = Celery(
        app.import_name,
        backend=app.config['CELERY_BROKER_URL'],
        broker=app.config['CELERY_RESULT_BACKEND']
    )

    TaskBase = async_celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    async_celery.Task = ContextTask
    async_celery.conf.update(app.config)

    return async_celery


# app_celery = make_celery()
