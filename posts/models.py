from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200, unique=True)
    book_author = models.CharField(max_length=100)
    content = models.TextField()
    fave_quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Book title: {self.book_title} | Post by {self.owner}"