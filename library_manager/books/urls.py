from django.urls import path
from . import views

    

urlpatterns = [
    path('hello/', views.hello_view, name='hello_world'),  # Fixed the name format for consistency
    path('books/new', views.create_book, name='create_book'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/delete/', views.delete_book, name='book_delete'),  # Use an identifier for specific actions
    path('books/<int:pk>/update/', views.update_book, name='update_book'),  # Use an identifier for updating
]

