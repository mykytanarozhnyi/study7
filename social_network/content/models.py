from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from usering.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_posts')
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='disliked_posts')

    def rating(self):
        return self.likes.count() - self.dislikes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):

    # id
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment #{self.id} for {self.post}"
