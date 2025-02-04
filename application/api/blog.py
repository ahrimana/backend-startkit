from flask_rest_api import Blueprint, abort

from ..models.blog import Blog
from ..schemas.blog import BlogSchema
from ..schemas.paging import PageInSchema, PageOutSchema, paginate
from .methodviews import ProtectedMethodView

blueprint = Blueprint('blog', 'blog')


@blueprint.route('', endpoint='blogs')
class BlogListAPI(ProtectedMethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(PageOutSchema(BlogSchema))
    def get(self, pagination):
        """List blogs"""
        return paginate(Blog.select(), pagination)

    @blueprint.arguments(BlogSchema)
    @blueprint.response(BlogSchema)
    def post(self, args):
        """Create blog"""
        blog = Blog(**args)
        blog.save()
        return blog


@blueprint.route('/<blog_id>', endpoint='blog')
class BlogAPI(ProtectedMethodView):
    @blueprint.response(BlogSchema)
    def get(self, blog_id):
        """Get blog details"""
        try:
            blog = Blog.get(id=blog_id)
        except Blog.DoesNotExist:
            abort(404, 'Blog not found')
        return blog

    @blueprint.arguments(BlogSchema(partial=True))
    @blueprint.response(BlogSchema)
    def patch(self, args, blog_id):
        try:
            blog = Blog.get(id=blog_id)
        except Blog.DoesNotExist:
            abort(404, 'Blog not found')
        for field in args:
            setattr(blog, field, args[field])
        blog.save()
        return blog

    @blueprint.response(BlogSchema)
    def delete(self, blog_id):
        try:
            blog = Blog.get(id=blog_id)
        except Blog.DoesNotExist:
            abort(404, 'Blog not found')
        blog.delete_instance()
        return blog
