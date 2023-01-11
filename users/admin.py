from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel
@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    fieldsets = (
        (
            "기본정보",
            {
                "fields":('username','name','email'),
            },
        ),
        (
            "권한",
            {
                "fields":('is_active','is_staff',
                          'is_superuser','groups','user_permissions'),
                "classes":('collapse',),
            },
        ),
        (
            "접속정보",
            {
                "fields":('date_joined','last_login'),
                "classes":('collapse',),
            },
        ),
    )
    
    list_filter=['is_active','is_staff']
    list_display=['username','name','email','date_joined','last_login']