from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    TextField
)

from ..db import db

from .auth import User

Model = db.Model


class Blog(Model):
    title = TextField()
    text = TextField()
    author = ForeignKeyField(User, related_name='blogs', null=True)
