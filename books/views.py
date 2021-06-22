from django.shortcuts import render
from .models import Book
# Create your views here.

def homepage(request):
    # show a homepage
    return render(request, "books/homepage.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})