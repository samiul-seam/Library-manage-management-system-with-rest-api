from rest_framework.response import Response
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from book.models import Category , Book , Author, BookImages, Review
from book.serializers import CategorySerializer, AuthorSerializer, BookSerializer, BookImageSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from book.filters import BookFilter
from .permissions import IsLibrarainOrReadOnly, IsReviewAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(
        book_count=Count('books')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsLibrarainOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve all categories",
        operation_description="Get a list of all categories with book count",
        responses={200: CategorySerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a single category",
        responses={200: CategorySerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new category",
        operation_description="Only librarian can create a category",
        request_body=CategorySerializer,
        responses={201: CategorySerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update a category",
        request_body=CategorySerializer,
        responses={200: CategorySerializer, 400: "Bad Request"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Delete a category",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

 
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.annotate(
        book_count=Count('books')).all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarainOrReadOnly]

    @swagger_auto_schema(
        operation_summary="Retrieve all authors",
        operation_description="Get a list of all authors with book count",
        responses={200: AuthorSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new author",
        operation_description="Only librarian can create an author",
        request_body=AuthorSerializer,
        responses={201: AuthorSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a single author",
        responses={200: AuthorSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Update an author",
        request_body=AuthorSerializer,
        responses={200: AuthorSerializer, 400: "Bad Request"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an author",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'description']
    permission_classes = [IsLibrarainOrReadOnly]

    def get_queryset(self):
        return Book.objects.prefetch_related('images').all()

    @swagger_auto_schema(
        operation_summary="Retrieve all books",
        operation_description="Get a list of all books. Supports filtering, searching, and ordering",
        responses={200: BookSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a single book",
        responses={200: BookSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Create a new book",
        operation_description="Only librarian can create a book",
        request_body=BookSerializer,
        responses={201: BookSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a book",
        request_body=BookSerializer,
        responses={200: BookSerializer, 400: "Bad Request"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a book",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BookImageViewSet(ModelViewSet):
    serializer_class = BookImageSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return BookImages.objects.filter(book_id=self.kwargs.get('book_pk'))

    def perform_create(self, serializer):
        serializer.save(book_id=self.kwargs["book_pk"])

    @swagger_auto_schema(
        operation_summary="Retrieve all images for a book",
        responses={200: BookImageSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Add an image to a book",
        request_body=BookImageSerializer,
        responses={201: BookImageSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs.get('book_pk'))

    def get_serializer_context(self):
        return {'book_id': self.kwargs.get('book_pk')}
    

    @swagger_auto_schema(
        operation_summary="Retrieve all reviews for a book",
        responses={200: ReviewSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a single review",
        responses={200: ReviewSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a review for a book",
        operation_description="User can add review to a book",
        request_body=ReviewSerializer,
        responses={201: ReviewSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a review",
        request_body=ReviewSerializer,
        responses={200: ReviewSerializer, 400: "Bad Request"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a review",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)