from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import ValidationError
from flask_ckeditor import CKEditorField

from .models import Blog


class AddPost(FlaskForm):
    title = StringField(label='', validators=[])
    image = FileField(label='', validators=[])
    body = CKEditorField(label='', validators=[])
    category = QuerySelectField(label='', validators=[], get_label='name')

    def validate_title(self, title_to_check):
        blog = Blog.query.filter_by(title=title_to_check.data).first()
        if blog:
            raise ValidationError('عنوان تکراری است ')


class AddCat(FlaskForm):
    name = StringField()
