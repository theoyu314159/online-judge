import mongoengine as me
from mongoengine.queryset.manager import QuerySetManager


class User(me.Document):
    objects: QuerySetManager

    username = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)
