from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from .models import Books
from .forms import CreateNewList, UpdateForm
def home(request):
    return render(request, "books/home.html", {})
   
def booklist(request):
    books= Books.objects.all()
    return render(request, "books/list.html", {"books":books})
def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            t = form.cleaned_data["title"]
            a = form.cleaned_data["author"]
            j = form.cleaned_data["isbn"]
            p = form.cleaned_data["publication_year"]
            g = form.cleaned_data["genre"]
            c = form.cleaned_data["copies"]
            b = Books(title=t,author=a,isbn=j,publication_year=p,genre=g,copies=c)
            b.save()

            return HttpResponseRedirect("/books/booklist" )
    else:
        form = CreateNewList
        return render(request, "books/create.html", {"form":form})
def delete_book(request, title):
    book = Books.objects.get(title=title)
    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect("/books/booklist" )