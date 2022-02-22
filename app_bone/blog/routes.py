from flask import render_template, flash
from flask_login import login_required

from app_bone import db
from .models import Blog, Category
from .forms import AddPost, AddCat
from . import blog


@blog.route('/')
def blog_list():
    blogs = Blog.query.all()
    categories = Category.query.all()
    # middleware test
    # print(request.salam)
    return render_template('blog/blog_list.html', blogs=blogs, categories=categories)


@blog.route('/<int:id>/')
def blog_detail(id):
    got_blog = Blog.query.filter_by(id=id).first_or_404()
    return render_template('blog/blog_detail.html', blog=got_blog)


@blog.route('/add-post/', methods=['GET', 'POST'])
@login_required
def add_post():
    post_form = AddPost()
    post_form.category.query = Category.query.all()
    if post_form.validate_on_submit():
        got_cat = Category.query.get(int(post_form.category.raw_data[0]))
        new_blog = Blog(title=post_form.title.data,
                        body=post_form.body.data,
                        category=got_cat,
                        image=post_form.image.data)
        got_cat.blogs.append(new_blog)
        # db.session.add(new_blog)
        # db.session.commit()
        new_blog.save()
        flash('پست با موفقیت ایجاد شد', category='success')
        post_form.data.popitem()
    if post_form.errors:
        for error in post_form.errors:
            flash(error, category='danger')
    return render_template('blog/add_blog_post.html', form=post_form)


@blog.route('/add-cat/', methods=['GET', 'POST'])
@login_required
def add_cat():
    cat_form = AddCat()
    if cat_form.validate_on_submit():
        db.session.add(Category(name=cat_form.name.data))
        db.session.commit()
        flash('اضافه شد', category='info')
    if not cat_form.errors:
        for error in cat_form.errors:
            flash(error, category='danger')
    return render_template('blog/add_blog_cat.html', form=cat_form)
