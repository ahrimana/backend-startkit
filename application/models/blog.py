from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    TextField
)

from ..db import db

Model = db.Model


class Blog(Model):
    title = TextField()
    text = TextField()
