from django.urls import path
from . import views

    

urlpatterns = [
    path("",views.home, name="home"),
    path("home/",views.home, name="home"),
    path("books/booklist",views.booklist, name='index'),
    path("create/", views.create, name="create"), 
    path('delete/<str:title>/', views.delete_book, name='delete_book'),
     # Use an identifier for updatings
]

