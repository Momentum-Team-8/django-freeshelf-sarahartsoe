from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from .forms import BookForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    # show a homepage
    return render(request, "books/homepage.html")

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def profile_page(request):
    return render(request, "books/profile_page.html")

@login_required
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
    return render(request, 'books/book_edit.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()
    return render(request, "books/show_category.html", {'books': books, 'category': category,})