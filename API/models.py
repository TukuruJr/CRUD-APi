from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
