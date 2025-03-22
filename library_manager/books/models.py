from django.db import models
#these are the two models which represent the available books and the borrowed boks in the library
class Books(models.Model):
    title = models.CharField(max_length=200)  
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)  #  ISBN for unique identification
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)  
    copies = models.IntegerField(default=1)  # Tracks the number of available copies

    def __str__(self):
        return self.title


