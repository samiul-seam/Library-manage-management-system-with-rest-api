from rest_framework.viewsets import GenericViewSet , ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .models import Borrow , BorrowBook
from .serializers import BorrowSerializer, BorrowBookSerializer, AddBorrowBookSerializer, UpdateBorrowBookSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class BorrowViewSet(ModelViewSet):
    serializer_class = BorrowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Borrow.objects.none()
        return Borrow.objects.prefetch_related('borrowbooks__book').filter(user=self.request.user)
    
    @swagger_auto_schema(
        operation_summary="Retrieve all borrows for the current user",
        operation_description="Get a list of all borrow records for the authenticated user, including related borrowed books",
        responses={200: BorrowSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a single borrow record",
        responses={200: BorrowSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a single borrow record",
        responses={200: BorrowSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new borrow record",
        operation_description="Authenticated users can create a new borrow record",
        request_body=BorrowSerializer,
        responses={201: BorrowSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a borrow record",
        request_body=BorrowSerializer,
        responses={200: BorrowSerializer, 400: "Bad Request"}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a borrow record",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BorrowBookViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBorrowBookSerializer
        elif self.request.method == 'PATCH':
            return UpdateBorrowBookSerializer
        return BorrowBookSerializer


    def get_serializer_context(self):
        return {'borrow_id': self.kwargs.get('borrow_pk')}


    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return BorrowBook.objects.none()
        return BorrowBook.objects.prefetch_related('book').filter(borrow_id=self.kwargs['borrow_pk'])

    @swagger_auto_schema(
        operation_summary="Retrieve all books in a borrow",
        operation_description="Get a list of all books associated with a specific borrow record",
        responses={200: BorrowBookSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Retrieve a single borrowed book",
        responses={200: BorrowBookSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a single borrowed book",
        responses={200: BorrowBookSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Add a book to a borrow",
        operation_description="Authenticated users can add a book to their borrow record",
        request_body=AddBorrowBookSerializer,
        responses={201: BorrowBookSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a borrowed book",
        operation_description="Update details (like quantity or return status) for a borrowed book",
        request_body=UpdateBorrowBookSerializer,
        responses={200: BorrowBookSerializer, 400: "Bad Request"}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Remove a book from a borrow",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)