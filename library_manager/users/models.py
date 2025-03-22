from django.db import models
from books.models import Books

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    date_of_membership = models.DateField()
    active_status = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length = 200)
    date_of_hire = models.DateField()
    salary = models.IntegerField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        return f"{self.member} borrowed {self.book.title}"
class BorrowedBooks(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)  # Link borrowed books to members
    book = models.ForeignKey(Books, on_delete=models.CASCADE)  # Reference AvailableBooks
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.member} borrowed {self.book.title}"