from django.contrib import admin
from userprofile.models import User, Profile
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UsersAdmin(UserAdmin):
    ordering = ('-date_joined',)
    search_fields = ('email', 'username',)
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ("Login Info", {'fields': ('email', 'username', 'password',)}),
        ('permission', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
    )
    # exclude = ('date_joined',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UsersAdmin)
admin.site.register(Profile)
