from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model : User
    list_display = ('uid', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields' : ('uid', 'password')}),
        ('personal Info', {'fields': ('first_name', 'last_name', 'batch', 'phone_number'),}),
        ('permission', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        ( None, {
            'classes' : ('wide',),
            'fields': ('uid','password1', 'password2', 'is_staff', 'is_active')
        }),
    )

    search_fields = ('uid',)
    ordering = ('uid',)


admin.site.register(User, CustomUserAdmin)