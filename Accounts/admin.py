from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active","first_name",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        ("Infos", {"fields": ("first_name", "last_name","email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Personal Infos", {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", "password1", "password2",
            )}
        ),
        ("Permissions", {
            "classes": ("wide",),
            "fields" : ("is_staff", "is_active", "groups", "user_permissions")
        })
    )
    search_fields = ("email","first_name","last_name",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Membership)
admin.site.register(ResultatQuiz)
admin.site.register(Semestre)
admin.site.register(Faculte)