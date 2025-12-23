from rest_framework import serializers
from book.models import Book
from .models import Borrow , BorrowBook

class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'is_available']
  

class AddBorrowBookSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()

    class Meta:
        model = BorrowBook
        fields = ['id', 'book_id', 'quantity']

    def save(self, **kwargs):
        borrow_id = self.context['borrow_id']
        book_id = self.validated_data['book_id']
        quantity = self.validated_data['quantity']

        try:
            borrow_book = BorrowBook.objects.get(borrow_id=borrow_id, book_id=book_id)
            borrow_book.quantity += quantity
            self.instance = borrow_book
            borrow_book.save()
        except BorrowBook.DoesNotExist:
            self.instance = BorrowBook.objects.create(
                borrow_id=borrow_id, **self.validated_data
            )

        return self.instance

    def validate_book_id(self, value):
        if not Book.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"Book with id:{value} does not exist")
        if not Book.objects.get(pk=value).is_available:
            raise serializers.ValidationError(f"Book '{Book.objects.get(pk=value).title}' is not available")
        return value


class BorrowBookSerializer(serializers.ModelSerializer):
    book = SimpleBookSerializer()
    total_books = serializers.SerializerMethodField(method_name='get_total_books')

    class Meta:
        model = BorrowBook
        fields = ['id', 'book', 'quantity', 'borrow_date', 'return_date', 'total_books']

    def get_total_books(self, borrow_book: BorrowBook):
        return borrow_book.quantity
    

class UpdateBorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowBook
        fields = ['quantity']


class BorrowSerializer(serializers.ModelSerializer):
    borrowbooks = BorrowBookSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.first_name', read_only=True)
    total_books = serializers.SerializerMethodField(method_name='get_total_books')

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'user_name', 'borrowbooks', 'total_books']

    def get_total_books(self, borrow: Borrow):
        return sum([item.quantity for item in borrow.borrowbooks.all()])