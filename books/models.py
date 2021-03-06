from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


CATEGORY_CHOICES = (
    ('generic','GENERIC'),
    ('python', 'PYTHON'),
    ('javascript', 'JAVASCRIPT'),
)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField("Category", related_name="books")
    url = models.CharField(max_length=600, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='generic')
    slug = models.SlugField(max_length=75)
