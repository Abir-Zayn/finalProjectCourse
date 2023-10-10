from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('scifi', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
    ]
    
    genre = models.CharField(max_length=100,choices=GENRE_CHOICES)
    quantity = models.IntegerField(default=10)
    ISBN = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1200123),
        ]
    )
    borrowed_by= models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class loan(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    returned_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} borrowed by {self.user}"

class returnbook(models.Model):
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    returned_date = models.DateTimeField(auto_now=True)
    review = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user} returned {self.book}"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete =models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='media/profile_pics')
    
    def __str__(self):
        return f'{self.user} Profile '

class wishlist(models.Model):
    user_name = models.CharField(max_length=40)
    book_req = models.CharField(max_length=20)
    date_req = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20)
    publish = models.DateTimeField()
    ISBN = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(1200123),
        ]
    )

