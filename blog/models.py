from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Post(models.Model):
    title = CharField(max_length=200)
    author = ForeignKey("auth.User", on_delete=models.CASCADE)
    body = TextField()

    def __str__(self):
        return self.title
