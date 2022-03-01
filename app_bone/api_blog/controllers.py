from flask.views import MethodView
from flask import request

from .Schemas import BlogSchema
from app_bone.blog.models import Blog

blog_api = BlogSchema()
blogs_api = BlogSchema(many=True)


class BlogListView(MethodView):
    def get(self):
        blogs = Blog.query.all()
        blogs_api.dump(blogs)
        return blogs_api.jsonify(blogs), 201


class BlogDetailView(MethodView):
    def get(self, id):
        blog = Blog.query.get(id)
        return blog_api.jsonify(blog)

    def post(self, id):
        blog = Blog.query.get(id)
        blog.title = request.json.get('title', blog.title)
        blog.body = request.json.get('body', blog.body)
        blog.save()
        return blog_api.jsonify(blog)
