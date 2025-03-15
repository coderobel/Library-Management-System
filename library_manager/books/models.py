from django.db import models
from users.models import Members 
#these are the two models which represent the available books and the borrowed boks in the library
class AvailableBooks(models.Model):
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)  #  ISBN for unique identification
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)  
    copies = models.IntegerField(default=1)  # Tracks the number of available copies

    def __str__(self):
        return self.title

class BorrowedBooks(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE)  # Link borrowed books to members
    book = models.ForeignKey(AvailableBooks, on_delete=models.CASCADE)  # Reference AvailableBooks
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.member} borrowed {self.book.title}"
