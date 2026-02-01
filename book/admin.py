from django.contrib import admin
from .models import Book, BookImages, Review, Category, Author
from django.db.models import Avg

class BookImagesInline(admin.TabularInline):
    model = BookImages
    extra = 1 
    readonly_fields = ['image'] 

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'is_available']
    list_filter = ['is_available', 'category', 'author']
    search_fields = ['title', 'author__name', 'isbn']
    inlines = [BookImagesInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'rating', 'comment', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['book__title', 'user__uid', 'comment']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'biography']
    search_fields = ['name']
