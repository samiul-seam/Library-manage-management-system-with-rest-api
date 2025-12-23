from django.db import models

# Create your models here.
from django.db import models
from uuid import uuid4
from user.models import User
from book.models import Book
from django.core.validators import MinValueValidator
from django.utils import timezone
from datetime import timedelta


# Create your models here.

# book, member, borrow date, return date
class Borrow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="borrows")

    def __str__(self):
        return f"Borrowed list of {self.user.first_name}"
    

def default_return_date():
    return timezone.now() + timedelta(days=7)


class BorrowBook(models.Model):
    borrow = models.ForeignKey(Borrow, on_delete=models.CASCADE, related_name="borrowbooks")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    borrow_date = models.DateTimeField(auto_now_add=True)
    
    return_date = models.DateTimeField(default=default_return_date)

    class Meta:
        unique_together = ['borrow', 'book']

    