from flask import Blueprint

from .controllers import BlogListView,BlogDetailView

api_blog = Blueprint('api_blog', __name__, url_prefix='/api')

api_blog.add_url_rule('/blog', view_func=BlogListView.as_view('blog_list_api'))
api_blog.add_url_rule('/blog/<int:id>', view_func=BlogDetailView.as_view('blog_detail_api'))
