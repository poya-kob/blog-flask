from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_bone.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
ck_editor = CKEditor()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config_class)

    # Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ck_editor.init_app(app)

    # bluePrints
    from app_bone.blog.routes import blog
    from app_bone.account.routes import user
    app.register_blueprint(blog)
    app.register_blueprint(user)
    return app
