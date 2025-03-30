from django.http import HttpResponse
from django.shortcuts import render
from .models import Books
from .forms import CreateNewList
def home(request):
    return render(request, "books/home.html", {})
   
def booklist(request):
    books= Books.objects.all()
    return render(request, "books/list.html", {"books":books})
def create(request):
    form = CreateNewList()
    return render(request, "books/create.html", {"form":form})

    
