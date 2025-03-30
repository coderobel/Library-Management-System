from django.urls import path
from . import views

    

urlpatterns = [
    path("",views.home, name = "home"),
    path("books/booklist",views.booklist, name='index'),
    path("create/", views.create, name="create"), 
     # Use an identifier for updatings
]

