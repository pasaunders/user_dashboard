from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    user = models.ForeignKey(
        User,
        related_name='messages'
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)


class Comments(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments'
    )
    date_uploaded = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255)