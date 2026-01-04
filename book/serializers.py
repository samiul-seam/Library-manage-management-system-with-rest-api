from rest_framework import serializers
from book.models import Category , Author , Book, BookImages, Review
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'book_count']

    book_count = serializers.IntegerField(read_only=True)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'book_count']

    book_count = serializers.IntegerField(read_only=True)
 


class BookImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = BookImages
        fields = ['id', 'image']


class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        method_name='get_current_user_name')

    class Meta:
        model = get_user_model()
        fields = ['id', 'name']

    def get_current_user_name(self, obj):
        return obj.get_full_name()
        

class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'isbn', 'images'] 


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(
        method_name='get_user')
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'comment']
        read_only_fields = ['user', 'book']


    def get_user(self, obj):
        return SimpleUserSerializer(obj.user).data
    

    def create(self, validated_data):
        book_id = self.context['book_id']
        return Review.objects.create(book_id=book_id, **validated_data)
        
