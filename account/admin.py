from django.contrib import admin
from account.models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password", "is_staff", "is_active"]}),
        (
            "Other info",
            {
                "fields": [
                    "first_name",
                    "last_name",
                ],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active"
                ]
            },
        ),
    ]

