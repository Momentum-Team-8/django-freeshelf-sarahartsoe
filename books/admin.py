from django.contrib import admin
from .models import Category, User, Book

# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)