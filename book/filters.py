from django_filters.rest_framework import FilterSet
from book.models import Book

class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'author_id': ['exact'],
            'category_id': ['exact']
        }