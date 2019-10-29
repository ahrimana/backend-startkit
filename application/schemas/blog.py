from marshmallow import fields

from .base import BaseSchema
from .auth import UserSchema

class BlogSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    title = fields.String(description='Title')
    text = fields.String(description='Text')
    author = fields.Nested(UserSchema, dump_only=True)
