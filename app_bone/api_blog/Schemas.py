from app_bone import ma
from app_bone.blog.models import Category
from flask_marshmallow.fields import Hyperlinks, URLFor


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category


class BlogSchema(ma.Schema):
    category = ma.Nested(CategorySchema)
    detail_link = ma.Hyperlinks({
        'self': ma.URLFor('api_blog.blog_detail_api', values=dict(id='<id>', _scheme='http', _external=True))
    })

    class Meta:
        fields = ('id', 'title', 'body', 'category', 'detail_link')

# class BlogSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model:Blog
