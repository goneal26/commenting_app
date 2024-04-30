from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(default="", blank=True)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)