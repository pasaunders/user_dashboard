from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messages(models.Model):
    user = models.ForeignKey(
        User,
        related_name='messages'
    )

class Comments(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments'
    )