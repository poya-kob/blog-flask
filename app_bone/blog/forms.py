from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_ckeditor import CKEditorField


class AddPost(FlaskForm):
    title = StringField(label='', validators=[])
    image = FileField(label='', validators=[])
    body = CKEditorField(label='', validators=[])
    category = QuerySelectField(label='', validators=[], get_label='name')


class AddCat(FlaskForm):
    name = StringField()
