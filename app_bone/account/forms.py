from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app_bone.account.models import User

images = UploadSet('image', IMAGES)


class RegisterForm(FlaskForm):
    username = StringField(label='نام کاربری', validators=[Length(max=20), DataRequired()])
    email_address = EmailField(label='ادرس ایمیل', validators=[Length(max=30), DataRequired(), Email()])
    password1 = PasswordField(label="رمز عبور", validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label="تکرار رمز عبور",
                              validators=[Length(min=8),
                                          DataRequired(),
                                          EqualTo('password1', message='تکرار کلمه عبور با کلمه عبور برابر نیست')])
    image = FileField(label='تصویر پروفایل', validators=[FileAllowed(images, 'فقط تصاویر')])
    first_name = StringField(label='نام', validators=[Length(max=30)])
    last_name = StringField(label='نام خانوادگی', validators=[Length(max=30)])

    def validate_username(self, username_to_check):

        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('نام کاربری تکراری')

    def validate_email_address(self, email_to_check):
        user = User.query.filter_by(email_address=email_to_check.data).first()
        if user:
            raise ValidationError('ایمل تکراری')


class LoginForm(FlaskForm):
    username = StringField(label='نام کاربری', validators=[DataRequired()])
    password = PasswordField(label="رمز عبور", validators=[DataRequired()])
