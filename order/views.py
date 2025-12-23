from rest_framework.viewsets import GenericViewSet , ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .models import Borrow , BorrowBook
from .serializers import BorrowSerializer, BorrowBookSerializer, AddBorrowBookSerializer, UpdateBorrowBookSerializer


# Create your views here.
class BorrowViewSet(CreateModelMixin, GenericViewSet, RetrieveModelMixin, DestroyModelMixin):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


class BorrowBookViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBorrowBookSerializer
        elif self.request.method == 'PATCH':
            return UpdateBorrowBookSerializer
        return BorrowBookSerializer

    def get_serializer_context(self):
        return {'borrow_id': self.kwargs['borrow_pk']}

    def get_queryset(self):
        return BorrowBook.objects.filter(borrow_id=self.kwargs['borrow_pk'])
