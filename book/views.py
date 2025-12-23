from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from book.models import Category , Book , Author
from book.serializers import CategorySerializer, AuthorSerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from book.filters import BookFilter


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
        book_count=Count('books')).all()
    serializer_class = CategorySerializer


class AuthorViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
        book_count=Count('books')).all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'description']

