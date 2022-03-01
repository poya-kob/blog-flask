from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from app_bone.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_mail import Mail
from celery import Celery
from flask_marshmallow import Marshmallow
from flask_moment import Moment

from .celery_conf import init_celery
from .test_middleware import Middleware, middleware_func

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
ck_editor = CKEditor()
mail = Mail()
ma = Marshmallow()
moment = Moment()


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
    ma.init_app(app)
    moment.init_app(app)
    # middleware
    app.wsgi_app = Middleware(app.wsgi_app)
    app.before_request_funcs = {
        'blog': [middleware_func, ]
    }
    # bluePrints
    from app_bone.blog.routes import blog
    from app_bone.account.routes import user
    from app_bone.api_blog.routes import api_blog
    app.register_blueprint(blog)
    app.register_blueprint(user)
    app.register_blueprint(api_blog)

    # send media path
    @app.route('/<path:filename>')
    def media_url(filename):
        return send_from_directory(app.config['UPLOAD_DIR'], filename, as_attachment=True)

    return app


def make_celery(app_name=__name__):
    backend = "redis://localhost:6379/0"
    broker = backend.replace("0", "1")
    return Celery(app_name, backend=backend, broker=broker)


celery = make_celery()
