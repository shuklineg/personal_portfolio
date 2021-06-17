from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, TextField


class Blog(Model):
    title = CharField(max_length=200)
    description = TextField()
    date = DateField()

    def __str__(self):
        return self.title
