from django.db import models
from books.models import AvailableBooks, BorrowedBooks

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length = 200)
    date_of_membership = models.DateField()
    borrowedbook = models.ForeignKey(BorrowedBooks)
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length = 200)
    date_of_hire = models.DateField()
    salary = models.IntegerField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name