from django.db import models
from django.contrib.auth.models import User

# comment class
class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE) # the user who wrote the comment
	text = models.TextField(default="", blank=True) # content
	likes = models.ManyToManyField(User, related_name='likes', blank=True) # likes (relational to users)