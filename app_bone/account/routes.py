from flask import Blueprint, render_template, flash, redirect, url_for

from flask_login import login_user, logout_user
from app_bone import db
from .forms import RegisterForm, LoginForm
from .models import User

user = Blueprint('user', __name__, template_folder='../../templates')


@user.route('/register/', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        reg_user = User(username=form.username.data,
                        password=form.password1.data,
                        email_address=form.email_address.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data)
        db.session.add(reg_user)
        db.session.commit()
        return redirect(url_for('blog.blog_list'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'{err_msg}', category='danger')
    return render_template('account/register.html', form=form)


@user.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        got_user = User.query.filter_by(username=form.username.data).first()
        if got_user and got_user.check_password(form.password.data):
            login_user(got_user)
            # todo: remember?
            return redirect(url_for('blog.blog_list'))

    return render_template('account/login.html', form=form)


@user.route('/logout/')
def logout_page():
    logout_user()
    flash('user logged out', category='info')
    return redirect(url_for('blog.blog_list'))
