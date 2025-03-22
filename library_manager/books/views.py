from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Books
from .forms import BookForm
# Create your views here.
def hello_view(request):
    return HttpResponse("Welcome user, to the Library Manager App")
def book_list(request):
    books = books.objects.all()
    return render(request, 'book_list.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})
def update_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance = book)
    return render(request, 'update_book.html', {'form': form})
def delete_book(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})
    