import datetime

from flask_sqlalchemy import models_committed

from app_bone import db
from .signals import send_mail
from .mixins import ModelMixin

models_committed.connect(send_mail)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    parent = db.relationship(lambda: Category, lazy=True, remote_side=id, backref=db.backref('sub_category'))

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class Blog(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=60), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('blogs'), lazy=True)
    image = db.Column(db.String(30), nullable=True)

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
    #     models_committed.send(self)
    #     return self

    def __repr__(self):
        return f"<Blog>: {self.title}"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    blog = db.relationship('Blog', backref='comments', lazy=True)
    body = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
