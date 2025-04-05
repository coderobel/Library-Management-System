from django import forms
from .models import Books
class CreateNewList(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    author = forms.CharField(label = "author", max_length=200)
    isbn = forms.CharField(label = "isbn", max_length=13)  #  ISBN for unique identification
    publication_year = forms.IntegerField(label = "publication_year")
    genre = forms.CharField(label = "genre", max_length=100)  
    copies = forms.IntegerField(label = "copies")
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author','isbn', 'publication_year', 'genre', 'copies'] 