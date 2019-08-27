from marshmallow import fields

from .base import BaseSchema

class BlogSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    title = fields.String(description='Title')
    text = fields.String(description='Text')
