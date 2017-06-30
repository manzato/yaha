from mongoengine import Document, BooleanField, StringField, DateTimeField, ListField, ReferenceField, IntField

class Device(Document):
    label = StringField(required=True, unique=True, max_length=200)
    meta = { 'allow_inheritance':True }

class Light(Device):
    is_on = BooleanField(required=True, default=False)
    pin = IntField(required=True)

class Category(Document):
    label = StringField(required=True, unique=True, max_length=200)
    devices = ListField(ReferenceField(Device))
    order = IntField()
