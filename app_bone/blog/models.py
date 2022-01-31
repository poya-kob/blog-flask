import datetime

from app_bone import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), unique=True, nullable=False)

    # parent_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=True)
    # children = db.relationship('Category', lazy=True)

    def __repr__(self):
        return self.name


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=60), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    # lower case because of table name
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('blogs'), lazy=True)
    image = db.Column(db.String(30), nullable=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    blog = db.relationship('Blog', backref='comments', lazy=True)
    body = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
