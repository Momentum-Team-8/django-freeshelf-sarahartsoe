from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.utils import timezone
# Create your views here.

def homepage(request):
    # show a homepage
    return render(request, "books/homepage.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def profile_page(request):
    return render(request, "books/profile_page.html")

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_date = timezone.now()
            book.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'collection/book_edit.html', {'book': book})