from django.contrib import admin
from .models import Borrow , BorrowBook

# Register your models here.
@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

admin.site.register(BorrowBook)