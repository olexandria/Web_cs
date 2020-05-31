from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime
def current_year():
    return datetime.date.today().year
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
from model_utils import Choices
class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50, blank=True, null=True)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, default='1')
Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)
Status = Choices (
    ('read'),
    ('want_to_read'),
    ('in_progress'),
    ('not_read')
)

		
class Library(models.Model):
    code = models.IntegerField(null=False, primary_key=True)
    book = models.CharField(max_length=30, null=True, unique=True)
    rating = models.IntegerField(null=True)
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.book

    class Meta:
        db_table = "Librarys"		
class Course(models.Model):
    code = models.CharField(max_length=5, null=False, primary_key=True)
    title = models.CharField(max_length=30, null=True, unique=True)
    duration = models.IntegerField(null=True)
    fee = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Courses"
		
class Post(models.Model):
    post_heading = models.CharField(max_length=200)
    post_text = models.TextField()
    def __unicode__(self):
        return unicode(self.post_heading)	
 		

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
        				 

