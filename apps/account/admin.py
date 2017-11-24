from apps.account import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)}
         ),
    )

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'last_login',)}),
        # ('Personal info', {'fields': ('',)}),
        ('Permissions', {'fields': ('groups', 'is_superuser', 'user_permissions',)}),
    )

    list_display = ('email', 'is_superuser', 'last_login', 'id',)
    list_filter = ('email', 'is_superuser',)
    ordering = ('email',)
    search_fields = ('email',)


admin.site.register(models.User, UserAdmin)
